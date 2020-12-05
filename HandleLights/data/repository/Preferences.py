from Core.data.device.NoSerialException import NoSerialException
from HandleLights.data.datasource import LocalDataSource, ApiDataSource, NoApiPreferencesException


def get_light_preferences():
    try:
        return ApiDataSource.get_light_preferences()
    except NoApiPreferencesException:
        print("Oh shit! Problem with the API")
        return LocalDataSource.get_light_preferences()
    except NoSerialException:
        print("Oh shit! Problem reading the Serial Number")
        return LocalDataSource.get_light_preferences()