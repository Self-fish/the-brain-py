from HandleLights.data.datasource import LocalDataSource


def get_light_preferences():
    return LocalDataSource.get_light_preferences()
