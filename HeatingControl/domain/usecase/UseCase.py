from dependency_injector.wiring import inject, Provide

from Core.data.driver.RelayStatus import RelayStatus
from HandleAlerts.HandleAlertsContainer import HandleAlertsContainer
from HandleAlerts.data.repository.AlertsRepository import AlertsRepository
from HeatingControl.HeatingControlContainer import HeatingControlContainer
from HeatingControl.data.repository import HeatingTemperatureRepository
from HeatingControl.data.repository.HeatingStatusRepository import HeatingStatusRepository
from HeatingControl.domain.model.WaterTemperaturePreferences import WaterTemperaturePreferences
from HeatingControl.domain.model.WaterTemperaturePreferencesSource import WaterTemperaturePreferencesSource
from MeasureWaterTemp.data.datasource import LocalDataSource


class HeatingControlUseCase:

    @inject
    def __init__(self, heating_status_repository:
                 HeatingStatusRepository = Provide[HeatingControlContainer.heating_status_repository],
                 alerts_repository: AlertsRepository = Provide[HandleAlertsContainer.alerts_repository]):
        self.__heating_status_repository = heating_status_repository
        self.__alerts_repository = alerts_repository
        self.__api_errors_count = 0

    def control_heating(self):
        desired_water_temperature: WaterTemperaturePreferences = HeatingTemperatureRepository.get_heating_temperature()
        current_water_temperature = LocalDataSource.water_temperature
        if current_water_temperature < desired_water_temperature.temperature:
            self.__heating_status_repository.update_heating_status(RelayStatus.ON)
        else:
            self.__heating_status_repository.update_heating_status(RelayStatus.OFF)
        self.__handle_possible_api_errors(desired_water_temperature)

    def __handle_possible_api_errors(self, preferences: WaterTemperaturePreferences):
        if preferences.source != WaterTemperaturePreferencesSource.API and self.__api_errors_count < 3:
            self.__api_errors_count += 1
        else:
            if self.__api_errors_count > 0:
                self.__api_errors_count -= 1

        if self.__api_errors_count == 10:
            self.__alerts_repository.create_local_alert("Temp Preference Error")
            self.__api_errors_count = 0
