import time

from Core.data.device.NoSerialException import NoSerialException
from Core.data.driver.DS18B20Controller import DS18B20Controller
from Core.data.exception.NoWaterTemperatureException import NoWaterTemperatureException
from MeasureWaterTemp.data.datasource import ApiDataSource, LocalDataSource
from MeasureWaterTemp.data.datasource.NoMeasuresApiException import NoMeasuresApiException


class MeasureWaterRepository:

    ONE_MINUTE = 60000

    def __init__(self, water_temperature_controller):
        self.__last_measure_sent = 0
        self.__water_temperature_controller: DS18B20Controller = water_temperature_controller

    def track_water_temp(self):
        current_time = time.time() * 1000

        if current_time > self.__last_measure_sent + self.ONE_MINUTE:
            try:
                LocalDataSource.water_temperature = self.__water_temperature_controller.read_device_temperature()
                ApiDataSource.send_water_temperature(LocalDataSource.water_temperature)
                self.__last_measure_sent = current_time
            except (NoMeasuresApiException, NoSerialException):
                return False
            except NoWaterTemperatureException:
                return False
        return True


