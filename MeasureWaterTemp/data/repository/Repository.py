from MeasureWaterTemp.data.controller import DS18B20Controller
from MeasureWaterTemp.data.datasource import ApiDataSource


class WaterTemperatureRepository:

    def __init__(self):
        self.__water_temperature = 0
        print("Hola")

    def track_water_temp(self):
        self.__water_temperature = DS18B20Controller.read_temperature()
        try:
            ApiDataSource.send_water_temperature(self.__water_temperature)
        except Exception:
            print("Repository: Exception!")

    def get_water_temp(self):
        return self.__water_temperature
