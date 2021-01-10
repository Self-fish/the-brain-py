from Core.data.device.NoSerialException import NoSerialException
from MeasureWaterTemp.data.controller import DS18B20Controller
from MeasureWaterTemp.data.datasource import ApiDataSource, LocalDataSource
from MeasureWaterTemp.data.datasource.NoMeasuresApiException import NoMeasuresApiException


def track_water_temp():
    LocalDataSource.water_temperature = DS18B20Controller.read_temperature()
    try:
        #ApiDataSource.send_water_temperature(LocalDataSource.water_temperature)
        return True
    except (NoMeasuresApiException, NoSerialException):
        return False

