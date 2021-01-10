import time

from Core.data.device.NoSerialException import NoSerialException
from MeasureWaterTemp.data.controller import DS18B20Controller
from MeasureWaterTemp.data.datasource import ApiDataSource, LocalDataSource
from MeasureWaterTemp.data.datasource.NoMeasuresApiException import NoMeasuresApiException


class MeasureWaterRepository:

    def __init__(self):
        self.__last_measure_sent = 0

    def track_water_temp(self):
        current_time = time.time() * 1000
        LocalDataSource.water_temperature = DS18B20Controller.read_temperature()
        if current_time > self.__last_measure_sent + 60000:
            try:
                ApiDataSource.send_water_temperature(LocalDataSource.water_temperature)
            except (NoMeasuresApiException, NoSerialException):
                return False
        return True


