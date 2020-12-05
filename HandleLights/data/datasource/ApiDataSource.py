import requests


def get_light_preferences():

    try:
        f = open('/proc/cpuinfo', 'r')
        for line in f:
            if line[0:6] == 'Serial':
                print(line[10:26])
        f.close()

    except:
        print("Error!")


    preferences = requests.get("http://192.168.0.16:8080/preferences?deviceId=sf-000000009df9b726")
    if preferences.status_code !=200:
        print("Fuck")
    else:
        print(preferences.json()['lightsPreferences']['range']['starting'])
