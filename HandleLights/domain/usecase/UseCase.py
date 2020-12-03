from HandleLights.data.controller.Controller import LightsController
from HandleLights.data.repository import Preferences
from HandleLights.domain.model.LightPreferences import LightPreferences
from datetime import datetime
from pytz import timezone

def should_turn_on_lights(current_time, light_preferences: LightPreferences):
    return light_preferences.starting_hour <= current_time < light_preferences.finishing_hour


class HandleLightsUseCase:

    def __init__(self):
        self.__controller = LightsController()

    def handle_lights(self):
        current_time = datetime.now(timezone('Europe/Madrid')).strftime("%H:%M")
        if should_turn_on_lights(current_time, Preferences.get_light_preferences()):
            print("Encendemos la luces")
        else:
            print("Apagamos las luces")


