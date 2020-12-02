import time

from HandleLights.data.repository.Controller import LightController


class HandleLightsUseCase:

    def __init__(self):
        # TODO something here
        print("Hola")

    def handle_lights(self):
        controller = LightController()
        controller.turn_on_lights()
        time.sleep(5)
        controller.turn_off_lights()