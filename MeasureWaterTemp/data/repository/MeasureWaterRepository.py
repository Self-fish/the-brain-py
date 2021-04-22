import time

from Core.data.device.NoSerialException import NoSerialException
from Core.data.driver.DS18B20Controller import DS18B20Controller
from MeasureWaterTemp.data.datasource import ApiDataSource, LocalDataSource
from MeasureWaterTemp.data.datasource.NoMeasuresApiException import NoMeasuresApiException


class MeasureWaterRepository:

    ONE_MINUTE = 60000

    def __init__(self, water_temperature_controller):
        self.__last_measure_sent = 0
        self.__water_temperature_controller: DS18B20Controller = water_temperature_controller

    def track_water_temp(self):
        print("Repository: reading the temperature")
        current_time = time.time() * 1000
        LocalDataSource.water_temperature = self.__water_temperature_controller.read_device_temperature()
        print("Repository: temperature read")
        if current_time > self.__last_measure_sent + self.ONE_MINUTE:
            try:
                print("Sending to the API")
                ApiDataSource.send_water_temperature(LocalDataSource.water_temperature)
                print("Sento to the API")
                self.__last_measure_sent = current_time
            except (NoMeasuresApiException, NoSerialException):
                return False
        return True


