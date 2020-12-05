import requests


def get_light_preferences():
    preferences = requests.get("http://192.168.0.16:8080/preferences?deviceId=sf-000000009df9b726")
    if preferences.status_code !=200:
        print("Fuck")
    else:
        for preference in preferences.json():
            print(preference["creationDate"])
