import spidev


spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

swt_channel = 0
vrx_channel = 1
vry_channel = 2


def __read_channel(channel):
    adc = spi.xfer2([1, (8+channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data


def is_switch_pressed():
    return __read_channel(swt_channel) == 0


def is_joystick_down():
    return __read_channel(vrx_channel) >= 1000


def is_joystick_up():
    return __read_channel(vrx_channel) <= 500


def is_joystick_right():
    return __read_channel(vry_channel) <= 500


def is_joystick_left():
    return __read_channel(vry_channel) >= 1000

