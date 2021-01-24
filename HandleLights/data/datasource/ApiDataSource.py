import requests

from requests.exceptions import ConnectionError, ConnectTimeout

from Core.data.device import ReadSerialNumber
from Core.data.device.NoSerialException import NoSerialException
from HandleLights.data.datamodel.LightPreferencesDataModel import LightPreferencesDataModel
from HandleLights.data.datasource.NoApiPreferencesException import NoApiPreferenceException
from HandleLights.domain.model.LightMode import LightMode

API_URI = "http://192.168.0.15:8083/preferences?deviceId=sf-"


MANUAL_OFF = "MANUAL_OFF"
MANUAL_ON = "MANUAL_ON"


def get_light_preferences():
    try:
        serial_number = ReadSerialNumber.get_serial_number()
        preferences = requests.get(API_URI + serial_number)
        if preferences.status_code != 200:
            raise NoApiPreferenceException
        else:
            if preferences.json()['lightsPreferences']['mode'] == MANUAL_OFF:
                light_mode = LightMode.MANUAL_OFF
            elif preferences.json()['lightsPreferences']['mode'] == MANUAL_ON:
                light_mode = LightMode.MANUAL_ON
            else:
                light_mode = LightMode.AUTOMATIC
            return LightPreferencesDataModel(preferences.json()['lightsPreferences']['range']['starting'],
                                             preferences.json()['lightsPreferences']['range']['finishing'],
                                             light_mode)

    except NoSerialException:
        raise NoSerialException

    except (ConnectionError, ConnectTimeout):
        raise NoApiPreferenceException
