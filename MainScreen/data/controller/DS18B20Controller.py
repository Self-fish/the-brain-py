import glob
import time


base_dir = '/sys/bus/w1/devices/'
devices_folder = glob.glob(base_dir + '28*')


def read_device_temperature(device):
    temperature = 0
    f = open(devices_folder[device] + '/w1_slave', 'r')
    lines = f.readlines()
    f.close()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temperature(device)
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp1_string = lines[1][equals_pos + 2:]
        temperature = float(temp1_string) / 1000.0
    return temperature


def read_temperature():
    temperature1 = read_device_temperature(0)
    temperature2 = read_device_temperature(1)
    print((temperature1 + temperature2) / 2)

