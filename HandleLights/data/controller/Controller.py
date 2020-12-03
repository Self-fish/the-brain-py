import time, wiringpi

from HandleLights.domain.model.LightStatus import LightStatus


class LightsController:

    def __init__(self):
        self.__io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)
        self.__io.pinMode(0, self.__io.OUTPUT)

    def update_light_status(self, light_status: LightStatus):
        print("Light Controller: " + light_status)
        if light_status == LightStatus.ON:
            self.__io.digitalWrite(0, self.__io.LOW)
        else:
            self.__io.digitalWrite(0, self.__io.HIGH)

    def get_current_light_status(self):
        print(self.__io.digitalRead(0))
