import requests

from Core.data.device import ReadSerialNumber
from HandleLights.data.datasource.NoApiPreferencesException import NoApiPreferenceException
from HandleLights.domain.model.LightPreferences import LightPreferences

URI = "http://192.168.0.25:8080/preferences?deviceId=sf-"


def get_light_preferences():
    try:
        serial_number = ReadSerialNumber.get_serial_number()
        preferences = requests.get(URI + serial_number)

        if preferences.status_code == 200:
            print("Tenemos preferencias")
            return LightPreferences(preferences.json()['lightsPreferences']['range']['starting'],
                                    preferences.json()['lightsPreferences']['range']['finishing'])
        else:
            print("No preferencias")
            return LightPreferences("-1", "-1")

    except requests.exceptions.ConnectionError as e:
        raise NoApiPreferenceException("Oeee")



