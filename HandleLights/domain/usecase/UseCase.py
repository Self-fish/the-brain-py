from dependency_injector.wiring import inject, Provide
from HandleLights.HandleLightsContainer import HandleLightsContainer
from HandleLights.data.repository import Preferences
from HandleLights.data.repository.LightStatus import LightStatusRepository
from HandleLights.domain.model.LightPreferences import LightPreferences
from datetime import datetime
from pytz import timezone
from HandleLights.domain.model.LightStatus import LightStatus


def should_turn_on_lights(current_time, light_preferences: LightPreferences):
    return light_preferences.starting_hour <= current_time < light_preferences.finishing_hour


class HandleLightsUseCase:

    @inject
    def __init__(self, light_repository: LightStatusRepository = Provide[HandleLightsContainer.light_status_repository]):
        self.__light_repository = light_repository

    def handle_lights(self):
        current_time = datetime.now(timezone('Europe/Madrid')).strftime("%H:%M")
        if should_turn_on_lights(current_time, Preferences.get_light_preferences()):
            self.__light_repository.update_light_status(LightStatus.ON)
            print("Encendemos las luces")
        else:
            self.__light_repository.update_light_status(LightStatus.OFF)
            print("Apagamos las luces")


