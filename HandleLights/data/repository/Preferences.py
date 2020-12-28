import requests

from HandleLights.data.datasource import LocalDataSource, ApiDataSource
from HandleLights.data.datasource.NoApiPreferencesException import NoApiPreferenceException


def get_light_preferences():
    try:
        return ApiDataSource.get_light_preferences()
    except NoApiPreferenceException:
        print("Oeeee")
        return LocalDataSource.get_light_preferences()