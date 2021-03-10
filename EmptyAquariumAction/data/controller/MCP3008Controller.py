import RPi.GPIO as GPIO
import time


def calculate_distance():
    GPIO.setmode(GPIO.BOARD)
    PIN_TRIGGER = 29
    PIN_ECHO = 37
    GPIO.setup(PIN_TRIGGER, GPIO.OUT)
    GPIO.setup(PIN_ECHO, GPIO.IN)
    NUMBER_OF_MEASUREMENTS = 20

    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    i = 0
    distance_aux = 0
    while i < NUMBER_OF_MEASUREMENTS:
        GPIO.output(PIN_TRIGGER, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(PIN_TRIGGER, GPIO.LOW)
        while GPIO.input(PIN_ECHO) == 0:
            pulse_start_time = time.time()
        while GPIO.input(PIN_ECHO) == 1:
            pulse_end_time = time.time()
        pulse_duration = pulse_end_time - pulse_start_time
        distance = round(pulse_duration * 17150, 2)
        distance_aux = distance_aux + distance
        i = i + 1
        time.sleep(0.2)

    final_distance = float("{:.2f}".format(distance_aux / NUMBER_OF_MEASUREMENTS))
    return final_distance
