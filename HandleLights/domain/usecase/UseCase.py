from dependency_injector.wiring import inject, Provide

from HandleAlerts.data.repository.AlertsRepository import AlertsRepository
from HandleLights.HandleLightsContainer import HandleLightsContainer
from HandleLights.data.repository import Preferences
from HandleLights.data.repository.LightStatus import LightStatusRepository
from HandleLights.domain.model.LightPreferences import LightPreferences
from datetime import datetime
from pytz import timezone
from Core.data.driver.RelayStatus import RelayStatus
from HandleLights.domain.model.LightPreferencesSource import LightPreferencesSource


def should_turn_on_lights(current_time, light_preferences: LightPreferences):
    return light_preferences.starting_hour <= current_time < light_preferences.finishing_hour


class HandleLightsUseCase:

    @inject
    def __init__(self,
                 light_repository: LightStatusRepository = Provide[HandleLightsContainer.light_status_repository],
                 alerts_repository: AlertsRepository = Provide[HandleLightsContainer.alerts_repository]):
        self.__light_repository = light_repository
        self.__alerts_repository = alerts_repository
        self.__api_errors_count = 0

    def handle_lights(self):
        current_time = datetime.now(timezone('Europe/Madrid')).strftime("%H:%M")
        preferences = Preferences.get_light_preferences()
        if should_turn_on_lights(current_time, preferences):
            self.__light_repository.update_light_status(RelayStatus.ON)
        else:
            self.__light_repository.update_light_status(RelayStatus.OFF)
        self.__handle_possible_api_errors(preferences)

    def __handle_possible_api_errors(self, preferences: LightPreferences):
        if preferences.source != LightPreferencesSource.API and self.__api_errors_count < 3:
            self.__api_errors_count += 1
            print("Incrementamos")
        else:
            if self.__api_errors_count > 0:
                self.__api_errors_count -= 1
                print("Decrementamos")

        if self.__api_errors_count == 3:
            print("Creamos una alerta local")
            self.__alerts_repository.create_local_alert("Preference Error")
            self.__api_errors_count = 0
