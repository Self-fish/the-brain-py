from Core.data.device.NoSerialException import NoSerialException
from HandleLights.data.datasource import LocalDataSource, ApiDataSource, NoApiPreferencesException


def get_light_preferences():
    try:
        return ApiDataSource.get_light_preferences()
    except Exception:
        print("Oh shit!")
        return LocalDataSource.get_light_preferences()
