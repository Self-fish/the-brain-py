import glob
import time


class DS18B20Controller:

    def __init__(self, device_id):
        self.__device_id = device_id

    def read_device_temperature(self):
        temperature = 0
        base_dir = '/sys/bus/w1/devices/'
        devices_folder = glob.glob(base_dir + self.__device_id)
        f = open(devices_folder[0] + '/w1_slave', 'r')
        lines = f.readlines()
        f.close()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.read_device_temperature()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos + 2:]
            temperature = float(temp_string) / 1000.0
        return round(temperature, 1)
