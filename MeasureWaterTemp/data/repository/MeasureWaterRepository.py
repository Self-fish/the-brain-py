import time

from Core.data.device.NoSerialException import NoSerialException
from MeasureWaterTemp.data.controller import DS18B20Controller
from MeasureWaterTemp.data.datasource import ApiDataSource, LocalDataSource
from MeasureWaterTemp.data.datasource.NoMeasuresApiException import NoMeasuresApiException


class MeasureWaterRepository:

    ONE_MINUTE = 60000

    def __init__(self):
        self.__last_measure_sent = 0

    def track_water_temp(self):
        current_time = time.time() * 1000
        LocalDataSource.water_temperature = DS18B20Controller.read_temperature()
        if current_time > self.__last_measure_sent + self.ONE_MINUTE:
            try:
                ApiDataSource.send_water_temperature(LocalDataSource.water_temperature)
                self.__last_measure_sent = current_time
            except (NoMeasuresApiException, NoSerialException):
                return False
        return True


