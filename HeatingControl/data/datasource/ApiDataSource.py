import requests

from Core.data.device import ReadSerialNumber
from Core.data.device.NoSerialException import NoSerialException
from HandleLights.data.datasource.NoApiPreferencesException import NoApiPreferenceException
from requests.exceptions import ConnectionError, ConnectTimeout

API_URI = "http://192.168.0.25:8080/preferences?deviceId=sf-"


def get_water_preferences():
    try:
        serial_number = ReadSerialNumber.get_serial_number()
        preferences = requests.get(API_URI + serial_number)
        if preferences.status_code != 200:
            raise NoApiPreferenceException
        else:
            return preferences.json()['waterPreferences']['value']

    except NoSerialException:
        raise NoSerialException

    except (ConnectionError, ConnectTimeout):
        raise NoApiPreferenceException
