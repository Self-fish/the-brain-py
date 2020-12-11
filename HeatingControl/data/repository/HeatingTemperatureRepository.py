from HeatingControl.data.datasource import LocalDataSource


def get_heating_temperature():
    return LocalDataSource.local_heating_temperature