from HandleLights.data.datasource import LocalDataSource
from HandleLights.data.datasource.ApiDataSource import ApiDataSource


class PreferencesRepository:

    def __init__(self, api_datasource: ApiDataSource):
        self.__api_datasource = api_datasource

    def get_light_preferences(self):
        try:
            return self.__api_datasource.get_light_preferences()
        except Exception:
            print("Use Case: No API")
            return LocalDataSource.get_light_preferences()