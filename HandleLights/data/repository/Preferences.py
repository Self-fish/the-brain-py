from Core.data.device.NoSerialException import NoSerialException
from Core.data.repository import LogsApiDataSource
from HandleLights.data.datasource import LocalDataSource, ApiDataSource
from HandleLights.data.datasource.NoApiPreferencesException import NoApiPreferenceException
from HandleLights.domain.model.LightPreferences import LightPreferences
from HandleLights.domain.model.LightPreferencesSource import LightPreferencesSource


def get_light_preferences():
    try:
        LogsApiDataSource.log_info("HandleLights  - PreferenceRepository: getting lights preferences from api")
        preferences = ApiDataSource.get_light_preferences()
        LogsApiDataSource.log_info("HandleLights  - PreferenceRepository: starting: " + preferences.starting_hour +
                                   ", finishing: " + preferences.finishing_hour +
                                   ", mode: " + preferences.light_mode.name)
        return LightPreferences(preferences.starting_hour, preferences.finishing_hour, preferences.light_mode,
                                LightPreferencesSource.API)
    except (NoApiPreferenceException, NoSerialException):
        LogsApiDataSource.log_warning("HandleLights  - PreferenceRepository: api failure")
        preferences = LocalDataSource.get_light_preferences()
        LogsApiDataSource.log_info("HandleLights  - PreferenceRepository: starting: " + preferences.starting_hour +
                                   ", finishing: " + preferences.finishing_hour +
                                   ", mode: " + preferences.light_mode.name)
        return LightPreferences(preferences.starting_hour, preferences.finishing_hour, preferences.light_mode,
                                LightPreferencesSource.LOCAL)
