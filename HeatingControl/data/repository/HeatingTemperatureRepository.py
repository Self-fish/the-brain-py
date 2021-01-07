from Core.data.device.NoSerialException import NoSerialException
from HandleLights.data.datasource.NoApiPreferencesException import NoApiPreferenceException
from HeatingControl.data.datasource import LocalDataSource, ApiDataSource
from HeatingControl.domain.model.WaterTemperaturePreferences import WaterTemperaturePreferences
from HeatingControl.domain.model.WaterTemperaturePreferencesSource import WaterTemperaturePreferencesSource


def get_heating_temperature():
    try:
        temperature = ApiDataSource.get_water_preferences()
        return WaterTemperaturePreferences(temperature, WaterTemperaturePreferencesSource.API)
    except (NoApiPreferenceException, NoSerialException):
        temperature = LocalDataSource.local_heating_temperature
        return WaterTemperaturePreferences(temperature, WaterTemperaturePreferencesSource.LOCAL)
