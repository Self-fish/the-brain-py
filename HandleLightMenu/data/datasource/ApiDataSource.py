import requests

from requests.exceptions import ConnectionError, ConnectTimeout
from Core.data.device import ReadSerialNumber
from Core.data.device.NoSerialException import NoSerialException

API_URI = "http://192.168.0.25:8080/preferences/updateLightPreferences"


def update_light_preferences(light_mode):
    print(light_mode)
    try:
        serial_number = ReadSerialNumber.get_serial_number()
        light_range = {"starting": "00:00", "finishing": "00:00"}
        light_preferences = {"mode": light_mode, "range": light_range}
        body = {"lightPreferences": light_preferences, "deviceId": "sf-" + serial_number}
        preferences = requests.put(API_URI, json=body)
        if preferences.status_code != 200:
            print("No 200")
            return False
        else:
            print("200")
            return True

    except NoSerialException:
        print("No Serial Exception")
        return False

    except (ConnectionError, ConnectTimeout):
        print("Other Exception")
        raise False