import requests

from Core.data.device import ReadSerialNumber
from Core.data.device.NoSerialException import NoSerialException
from Core.data.net import NetworkController, NoApiException
from HandleLights.domain.model.LightPreferences import LightPreferences

QUERY_PARAMS = "preferences?deviceId=sf-"


class ApiDataSource:

    def __init__(self, network_controller: NetworkController):
        self.__network_controller = network_controller

    def get_light_preferences(self):
        try:
            serial_number = ReadSerialNumber.get_serial_number()
            preferences = self.__network_controller.get_request(QUERY_PARAMS + serial_number)
            if preferences.status_code == 200:
                return LightPreferences(preferences.json()['lightsPreferences']['range']['starting'],
                                        preferences.json()['lightsPreferences']['range']['finishing'])
            else:
                print("No preferencesss")

        except NoSerialException:
            raise NoSerialException
