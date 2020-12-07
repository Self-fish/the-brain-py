import glob
import time


base_dir = '/sys/bus/w1/devices/'
first_device_folder = glob.glob(base_dir + '28*')[0]
second_device_folder = glob.glob(base_dir + '28*')[1]
first_device_file = first_device_folder + '/w1_slave'
second_device_file = second_device_folder + '/w1_slave'


def read_first_temperature_raw():
    f = open(first_device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_second_temperature_raw():
    f = open(second_device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temperature():
    lines1 = read_first_temperature_raw()
    lines2 = read_second_temperature_raw()
    while lines1[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines1 = read_first_temperature_raw()
    equals_pos = lines1[1].find('t=')
    if equals_pos != -1:
        temp_string = lines1[1][equals_pos + 2:]
        temp_c = float(temp_string) / 1000.0
        print(temp_c)

    while lines2[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines2 = read_second_temperature_raw()
    equals_pos2 = lines2[1].find('t=')
    if equals_pos2 != -1:
        temp_string2 = lines2[1][equals_pos2 + 2:]
        temp_c2 = float(temp_string2) / 1000.0
        print(temp_c2)