from dependency_injector.wiring import inject, Provide
from HandleLights.HandleLightsContainer import HandleLightsContainer
from HandleLights.data.repository.LightStatus import LightStatusRepository
from HandleLights.data.repository.Preferences import PreferencesRepository
from HandleLights.domain.model.LightPreferences import LightPreferences
from datetime import datetime
from pytz import timezone
from Core.data.driver.RelayStatus import RelayStatus


def should_turn_on_lights(current_time, light_preferences: LightPreferences):
    print("Should turn on lights")
    print(light_preferences.starting_hour)
    return light_preferences.starting_hour <= current_time < light_preferences.finishing_hour


class HandleLightsUseCase:

    @inject
    def __init__(self,
                 light_repository: LightStatusRepository = Provide[HandleLightsContainer.light_status_repository],
                 preferences_repository: PreferencesRepository = Provide[HandleLightsContainer.preferences_repository]):
        self.__light_repository = light_repository
        self.__preferences_repository = preferences_repository

    def handle_lights(self):
        current_time = datetime.now(timezone('Europe/Madrid')).strftime("%H:%M")
        if should_turn_on_lights(current_time, self.__preferences_repository.get_light_preferences()):
            self.__light_repository.update_light_status(RelayStatus.ON)
        else:
            self.__light_repository.update_light_status(RelayStatus.OFF)


