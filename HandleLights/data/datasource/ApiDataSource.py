import requests

from Core.data.device import ReadSerialNumber
from Core.data.device.NoSerialException import NoSerialException
from HandleLights.data.datasource import NoApiPreferencesException
from HandleLights.domain.model.LightPreferences import LightPreferences


def get_light_preferences():
    try:
        serial_number = ReadSerialNumber.get_serial_number()
        preferences = requests.get("http://192.168.0.16:8080/preferences?deviceId=sf-" +
                                   serial_number)
        if preferences.status_code != 200:
            raise NoApiPreferencesException
        else:
            return LightPreferences(preferences.json()['lightsPreferences']['range']['starting'],
                                    preferences.json()['lightsPreferences']['range']['finishing'])

    except NoSerialException:
        raise NoSerialException
