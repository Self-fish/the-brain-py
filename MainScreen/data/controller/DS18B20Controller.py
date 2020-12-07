import glob
import time


base_dir = '/sys/bus/w1/devices/'
devices_folder = glob.glob(base_dir + '28*')


def read_temperature(device):
    f = open(devices_folder[device] + '/w1_slave', 'r')
    lines = f.readlines()
    f.close()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temperature(device)
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp1_string = lines[1][equals_pos + 2:]
        temp1_c = float(temp1_string) / 1000.0
        print(temp1_c)
    return lines


def read_temperature():
    read_temperature(0)

