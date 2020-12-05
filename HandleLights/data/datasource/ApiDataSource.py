import requests
from pyserial import serial


def get_light_preferences():

    a = serial.tools.list_ports.comports()
    ports = []
    for w in a:
        ports.append((w.vid, w.device, w.serial_number))
    i = 0
    for w in ports:
        print('%d)\t%s\t(USB VID=%04X)\t Serial#:=%s' % (i, w[1], w[0] if (type(w[0]) is int) else 0, w[2]))
        i = i + 1

    preferences = requests.get("http://192.168.0.16:8080/preferences?deviceId=sf-000000009df9b726")
    if preferences.status_code !=200:
        print("Fuck")
    else:
        print(preferences.json()['lightsPreferences']['range']['starting'])
