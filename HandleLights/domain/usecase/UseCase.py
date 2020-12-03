from HandleLights.data.controller.Controller import LightsController
from HandleLights.data.repository import Preferences
from HandleLights.domain.model.LightPreferences import LightPreferences
from datetime import datetime
import pytz

def should_turn_on_lights(current_time, light_preferences: LightPreferences):
    return light_preferences.starting_hour <= current_time < light_preferences.finishing_hour


class HandleLightsUseCase:

    def __init__(self):
        self.__controller = LightsController()

    def handle_lights(self):
        timezone = pytz.timezone("Europe/Madrid")
        current_time = timezone.localize(datetime.now()).strftime("%H:%M")
        preferences = Preferences.get_light_preferences()
        print(current_time)
        print(preferences.starting_hour + ":" + preferences.finishing_hour)

        if should_turn_on_lights(current_time, Preferences.get_light_preferences()):
            print("Encendemos la luces")
        else:
            print("Apagamos las luces")


