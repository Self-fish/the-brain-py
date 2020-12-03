import time, wiringpi


class LightsController:

    def __init__(self):
        self.__io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)
        self.__io.pinMode(0, self.__io.OUTPUT)

    def turn_on_lights(self):
        self.__io.digitalWrite(0, self.__io.LOW)

    def turn_off_lights(self):
        self.__io.digitalWrite(0, self.__io.HIGH)

