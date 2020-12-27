import requests

from HandleLights.data.datasource import LocalDataSource, ApiDataSource


def get_light_preferences():
    try:
        ApiDataSource.get_light_preferences()
    except requests.exceptions.ConnectionError:
        print("Use Case: No API")
        return LocalDataSource.get_light_preferences()