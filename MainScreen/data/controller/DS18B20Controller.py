import glob
import time


def __read_device_temperature(device):
    temperature = 0
    base_dir = '/sys/bus/w1/devices/'
    devices_folder = glob.glob(base_dir + '28*')
    f = open(devices_folder[device] + '/w1_slave', 'r')
    lines = f.readlines()
    f.close()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temperature(device)
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2:]
        temperature = float(temp_string) / 1000.0
    return temperature


def read_temperature():
    return round((__read_device_temperature(0) * __read_device_temperature(1)) / 2, 1)

