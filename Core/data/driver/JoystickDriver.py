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
    if __read_channel(swt_channel) == 0:
        return True
    else:
        return False
