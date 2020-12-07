import glob
import time


base_dir = '/sys/bus/w1/devices/'
devices_folder = glob.glob(base_dir + '28*')


def read_temperature_raw(device):
    f = open(devices_folder[device] + '/w1_slave', 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temperature():
    temp_raw = (read_temperature_raw(0), read_temperature_raw(1))
    while temp_raw[0][0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        temp_raw = (read_temperature_raw(0), read_temperature_raw(1))
    equals_pos = temp_raw[0][1].find('t=')
    if equals_pos != -1:
        temp1_string = temp_raw[0][1][equals_pos + 2:]
        temp1_c = float(temp1_string) / 1000.0
        temp2_string = temp_raw[0][1][equals_pos + 2:]
        temp2_c = float(temp2_string) / 1000.0
        print(temp1_c)
        print(temp2_c)

