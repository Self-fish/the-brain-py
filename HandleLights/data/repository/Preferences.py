from Core.data.device.NoSerialException import NoSerialException
from HandleLights.data.datasource import LocalDataSource, ApiDataSource
from HandleLights.data.datasource.NoApiPreferencesException import NoApiPreferenceException
from HandleLights.domain.model.LightPreferences import LightPreferences
from HandleLights.domain.model.LightPreferencesSource import LightPreferencesSource


def get_light_preferences():
    try:
        preferences = ApiDataSource.get_light_preferences()
        return LightPreferences(preferences.starting_hour, preferences.finishing_hour, preferences.light_mode,
                                LightPreferencesSource.API)
    except (NoApiPreferenceException, NoSerialException):
        preferences = LocalDataSource.get_light_preferences()
        return LightPreferences(preferences.starting_hour, preferences.finishing_hour, preferences.light_mode,
                                LightPreferencesSource.LOCAL)
