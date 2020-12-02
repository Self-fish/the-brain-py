import RPi.GPIO as GPIO

class LightController:

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(0, GPIO.OUT)

    def turn_on_lights(self):
        GPIO.output(0, GPIO.LOW)
        print("Encedemos las luces")


    def turn_off_lights(self):
        GPIO.output(0, GPIO.HIGH)
        print("Apagamos las luces")
