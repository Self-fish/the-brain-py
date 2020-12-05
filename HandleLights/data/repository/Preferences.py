from HandleLights.data.datasource import LocalDataSource, ApiDataSource


def get_light_preferences():
    try:
        return ApiDataSource.get_light_preferences()
    except Exception:
        return LocalDataSource.get_light_preferences()