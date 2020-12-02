import time, wiringpi


class HandleLightsUseCase:

    def __init__(self):
        # TODO something here
        print("Hola")

    def handle_lights(self):
        io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)
        io.pinMode(0, io.OUTPUT)
        print("Encedemos las luces")
        io.digitalWrite(0, io.LOW)
        time.sleep(5)
        print("Apagamos las luces")
        io.digitalWrite(0, io.HIGH)
