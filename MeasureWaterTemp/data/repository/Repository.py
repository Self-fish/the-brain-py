from MeasureWaterTemp.data.controller import DS18B20Controller
from MeasureWaterTemp.data.datasource import ApiDataSource, LocalDataSource


def track_water_temp():
    LocalDataSource.water_temperature = DS18B20Controller.read_temperature()
    try:
        ApiDataSource.send_water_temperature(LocalDataSource.water_temperature)
    except Exception:
        print("Repository: Exception!")


