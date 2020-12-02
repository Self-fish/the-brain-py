import time, wiringpi


class HandleLightsUseCase:

    def __init__(self):
        # TODO something here
        print("Hola")

    def handle_lights(self):
        io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)
        io.pinMode(0, io.OUTPUT)
        io.digitalWrite(0, io.HIGH)
        time.sleep(5)
        io.digitalWrite(0, io.LOW)
