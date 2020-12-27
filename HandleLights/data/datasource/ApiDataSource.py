import requests

from Core.data.device import ReadSerialNumber
from Core.data.device.NoSerialException import NoSerialException
from Core.data.net import NetworkController, NoApiException
from HandleLights.data.datasource import NoApiPreferencesException
from HandleLights.domain.model.LightPreferences import LightPreferences

QUERY_PARAMS = "preferences?deviceId=sf-"


def get_light_preferences():
    try:
        serial_number = ReadSerialNumber.get_serial_number()
        preferences = NetworkController.get_request(QUERY_PARAMS + serial_number)
        return LightPreferences(preferences['lightsPreferences']['range']['starting'],
                                preferences['lightsPreferences']['range']['finishing'])

    except NoSerialException:
        print("Exception")
        raise NoSerialException
