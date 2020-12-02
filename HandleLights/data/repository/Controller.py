import wiringpi

io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)
io.pinMode(11, io.OUTPUT)


def turn_on_lights():
    io.digitalWrite(11, io.HIGH)
    print("Encedemos las luces")


def turn_off_lights():
    io.digitalWrite(11, io.LOW)
    print("Apagamos las luces")






