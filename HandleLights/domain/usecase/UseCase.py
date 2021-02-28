from dependency_injector.wiring import inject, Provide

from Core.data.repository import NotificationsApiDataSource, LogsApiDataSource
from HandleLights.HandleLightsContainer import HandleLightsContainer
from HandleLights.data.repository import Preferences
from HandleLights.data.repository.LightStatus import LightStatusRepository
from HandleLights.domain.model.LightMode import LightMode
from HandleLights.domain.model.LightPreferences import LightPreferences
from datetime import datetime
from pytz import timezone
from Core.data.driver.RelayStatus import RelayStatus
from HandleLights.domain.model.LightPreferencesSource import LightPreferencesSource


def should_turn_on_lights(current_time, light_preferences: LightPreferences):
    if light_preferences.light_mode == LightMode.MANUAL_ON:
        return True
    elif light_preferences.light_mode == LightMode.MANUAL_OFF:
        return False
    else:
        return light_preferences.starting_hour <= current_time < light_preferences.finishing_hour


class HandleLightsUseCase:

    max_errors = 3
    error_message = "Light Preference Error"

    @inject
    def __init__(self,
                 light_repository: LightStatusRepository = Provide[HandleLightsContainer.light_status_repository]):
        self.__light_repository = light_repository
        self.__api_errors_count = 0

    def handle_lights(self):
        current_time = datetime.now(timezone('Europe/Madrid')).strftime("%H:%M")
        LogsApiDataSource.log_info("HandleLights - UseCase checking if lights should be on/off at " + current_time)
        preferences = Preferences.get_light_preferences()
        if should_turn_on_lights(current_time, preferences):
            LogsApiDataSource.log_info("HandleLights  - UseCase: lights must be on")
            self.__light_repository.update_light_status(RelayStatus.ON)
        else:
            LogsApiDataSource.log_info("HandleLights - UseCase: lights must be off")
            self.__light_repository.update_light_status(RelayStatus.OFF)
        self.__handle_possible_api_errors(preferences)

    def __handle_possible_api_errors(self, preferences: LightPreferences):
        if preferences.source != LightPreferencesSource.API and self.__api_errors_count < self.max_errors:
            self.__api_errors_count += 1
            LogsApiDataSource.log_warning("HandleLights - UseCase: api error number: " + str(self.__api_errors_count))
        else:
            if self.__api_errors_count > 0:
                self.__api_errors_count -= 1
                LogsApiDataSource.log_info("HandleLights - UseCase: api error number: " + str(self.__api_errors_count))

        if self.__api_errors_count == self.max_errors:
            NotificationsApiDataSource.create_notification("Something seems to be wrong with the remote preferences."
                                                           "Impossible to get the lights range of hours")
            LogsApiDataSource.log_error("HandleLights - UseCase: api error number: " + str(self.__api_errors_count) +
                                        ". Creating remote notification")
            self.__api_errors_count = 0
