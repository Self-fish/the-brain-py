from HandleLights.data.datasource import LocalDataSource, ApiDataSource


def get_light_preferences():
    return ApiDataSource.get_light_preferences()
