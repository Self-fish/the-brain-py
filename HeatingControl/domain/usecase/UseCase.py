from dependency_injector.wiring import inject, Provide

from Core.data.driver.RelayStatus import RelayStatus
from HeatingControl.HeatingControlContainer import HeatingControlContainer
from HeatingControl.data.repository import HeatingTemperatureRepository
from HeatingControl.data.repository.HeatingStatusRepository import HeatingStatusRepository
from MeasureWaterTemp.data.datasource import LocalDataSource


class HeatingControlUseCase:

    @inject
    def __init__(self, heating_status_repository:
                 HeatingStatusRepository = Provide[HeatingControlContainer.heating_status_repository]):
        self.__heating_status_repository = heating_status_repository

    def control_heating(self):
        desired_water_temperature = HeatingTemperatureRepository.get_heating_temperature()
        current_water_temperature = LocalDataSource.water_temperature
        if current_water_temperature < desired_water_temperature:
            print("Encendemos el calentador")
            self.__heating_status_repository.update_heating_status(RelayStatus.ON)
        else:
            print("Apagamos el calendador")
            self.__heating_status_repository.update_heating_status(RelayStatus.OFF)

