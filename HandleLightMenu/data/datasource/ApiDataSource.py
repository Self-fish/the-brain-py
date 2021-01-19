import requests

from requests.exceptions import ConnectionError, ConnectTimeout
from Core.data.device import ReadSerialNumber
from Core.data.device.NoSerialException import NoSerialException
from HandleLights.data.datasource.NoApiPreferencesException import NoApiPreferenceException

API_URI = "http://192.168.0.25:8083/preferences/updateLightPreferences"


def update_light_preferences(light_mode):
    try:
        serial_number = ReadSerialNumber.get_serial_number()
        light_range = {"starting": "15:00", "finishing": "23:00"}
        light_preferences = {"mode": light_mode, "range": light_range}
        body = {"lightsPreferences": light_preferences, "deviceId": "sf-" + serial_number}
        preferences = requests.put(API_URI, json=body)
        if preferences.status_code != 200:
            raise NoApiPreferenceException
        else:
            return True

    except NoSerialException:
        raise NoSerialException

    except (ConnectionError, ConnectTimeout):
        raise NoApiPreferenceException
