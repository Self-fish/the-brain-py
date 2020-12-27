import requests

from Core.data.device import ReadSerialNumber
from Core.data.device.NoSerialException import NoSerialException
from MeasureWaterTemp.data.datasource.NoMeasuresApiException import NoMeasuresApiException

API_URI = "http://192.168.0.25:8081/measures/"


def send_water_temperature(water_temp):
    try:
        serial_number = ReadSerialNumber.get_serial_number()
        body = {"type": "WATER_TEMP", "value": water_temp, "deviceId": "sf-" + serial_number}
        resp = requests.post(API_URI, json=body)
        if resp.status_code != 200:
            raise NoMeasuresApiException

    except NoSerialException:
        raise NoSerialException
