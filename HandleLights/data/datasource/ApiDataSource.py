import requests

from Core.data.device import ReadSerialNumber
from Core.data.device.NoSerialException import NoSerialException
from HandleLights.data.datasource.NoApiPreferencesException import NoApiPreferenceException
from HandleLights.domain.model.LightPreferences import LightPreferences

URI = "http://192.168.0.25:8080/preferences?deviceId=sf-"


class NoApiPreferencesException(object):
    pass


def get_light_preferences():
    try:
        serial_number = ReadSerialNumber.get_serial_number()

        try:
            preferences = requests.get(URI + serial_number)
        except requests.exceptions.ConnectionError:
            print("No connection exception")
            raise NoApiPreferenceException

        if preferences.status_code == 200:
            print("Tenemos preferencias")
            return LightPreferences(preferences.json()['lightsPreferences']['range']['starting'],
                                        preferences.json()['lightsPreferences']['range']['finishing'])
        else:
            print("No preferencias")
            raise NoApiPreferencesException

    except NoSerialException:
        print("No serial exception")
        raise NoSerialException
