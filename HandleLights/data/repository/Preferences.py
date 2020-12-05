from HandleLights.data.datasource import LocalDataSource, ApiDataSource


def get_light_preferences():
    ApiDataSource.get_light_preferences()
    return LocalDataSource.get_light_preferences()
