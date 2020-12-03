import time, wiringpi

from HandleLights.data.controller.Controller import LightsController


class HandleLightsUseCase:

    def __init__(self):
        self.__controller = LightsController()

    def handle_lights(self):
        #io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)
        #io.pinMode(0, io.OUTPUT)
        #print("Encedemos las luces")
        #io.digitalWrite(0, io.LOW)
        self.__controller.turn_on_lights()
        time.sleep(5)
        self.__controller.turn_off_lights()
        #io.digitalWrite(0, io.HIGH)
