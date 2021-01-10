from Core.data.device.NoSerialException import NoSerialException
from HandleLights.data.datasource.NoApiPreferencesException import NoApiPreferenceException
from HeaterControl.data.datasource import LocalDataSource, ApiDataSource
from HeaterControl.domain.model.WaterTemperaturePreferences import WaterTemperaturePreferences
from HeaterControl.domain.model.WaterTemperaturePreferencesSource import WaterTemperaturePreferencesSource


def get_heating_temperature():
    try:
        temperature = ApiDataSource.get_water_preferences()
        return WaterTemperaturePreferences(temperature, WaterTemperaturePreferencesSource.API)
    except (NoApiPreferenceException, NoSerialException):
        temperature = LocalDataSource.local_heater_temperature
        return WaterTemperaturePreferences(temperature, WaterTemperaturePreferencesSource.LOCAL)
