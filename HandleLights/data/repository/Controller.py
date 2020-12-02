import wiringpi


class LightController:

    def __init__(self):
        self.io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)
        self.io.pinMode(11, self.io.OUTPUT)

    def turn_on_lights(self):
        self.io.digitalWrite(11, self.io.HIGH)
        print("Encedemos las luces")


    def turn_off_lights(self):
        self.io.digitalWrite(11, self.io.LOW)
        print("Apagamos las luces")
