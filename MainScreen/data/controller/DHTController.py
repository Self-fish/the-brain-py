import adafruit_dht
import board
import time

DHT = 2


def read_temperature():
    dht_device = adafruit_dht.DHT22(board.D3)
    while True:
        temperature = dht_device.temperature
        humidity = dht_device.humidity
        time.sleep(5) #Wait 5 seconds and read again
