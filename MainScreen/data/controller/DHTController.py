import adafruit_dht
import board

DHT = 2


def read_temperature():
    dht_device = adafruit_dht.DHT22(board.G2)
    while True:
        temperature = dht_device.temperature
        humidity = dht_device.humidity
        sleep(5) #Wait 5 seconds and read again
