import time

from HandleLights.data.repository.Controller import turn_on_lights, turn_off_lights


class HandleLightsUseCase:

    def __init__(self):
        # TODO something here
        print("Hola")

    def handle_lights(self):
        turn_on_lights()
        time.sleep(5)
        turn_off_lights()