from HeatingControl.data.datasource import LocalDataSource, ApiDataSource


def get_heating_temperature():
    try:
        return ApiDataSource.get_water_preferences()
    except Exception:
        return LocalDataSource.local_heating_temperature