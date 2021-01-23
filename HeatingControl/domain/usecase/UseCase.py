from dependency_injector.wiring import inject, Provide

from Core.data.driver.RelayStatus import RelayStatus
from Core.data.logs import LogsApiDataSource
from HandleAlerts.HandleAlertsContainer import HandleAlertsContainer
from HandleAlerts.data.repository.AlertsRepository import AlertsRepository
from HeatingControl.HeatingControlContainer import HeatingControlContainer
from HeatingControl.data.repository import HeatingTemperatureRepository
from HeatingControl.data.repository.HeatingStatusRepository import HeatingStatusRepository
from HeatingControl.domain.model.WaterTemperaturePreferences import WaterTemperaturePreferences
from HeatingControl.domain.model.WaterTemperaturePreferencesSource import WaterTemperaturePreferencesSource
from MeasureWaterTemp.data.datasource import LocalDataSource


class HeatingControlUseCase:

    max_errors = 10
    error_message = "Temp Preference Error"

    @inject
    def __init__(self, heating_status_repository:
                 HeatingStatusRepository = Provide[HeatingControlContainer.heating_status_repository],
                 alerts_repository: AlertsRepository = Provide[HandleAlertsContainer.alerts_repository]):
        self.__heating_status_repository = heating_status_repository
        self.__alerts_repository = alerts_repository
        self.__api_errors_count = 0

    def control_heating(self):
        LogsApiDataSource.log_info("HeatingControl - UseCase: comparing if water temperature fits requirements")
        desired_water_temperature: WaterTemperaturePreferences = HeatingTemperatureRepository.get_heating_temperature()
        LogsApiDataSource.log_info("HeatingControl - UseCase: "
                                   "the desired temperature is " + str(desired_water_temperature.temperature))
        current_water_temperature = LocalDataSource.water_temperature
        LogsApiDataSource.log_info("HeatingControl - UseCase: "
                                   "the current temperature is " + str(current_water_temperature))
        if current_water_temperature < desired_water_temperature.temperature:
            self.__heating_status_repository.update_heating_status(RelayStatus.ON)
        else:
            self.__heating_status_repository.update_heating_status(RelayStatus.OFF)
        self.__handle_possible_api_errors(desired_water_temperature)

    def __handle_possible_api_errors(self, preferences: WaterTemperaturePreferences):
        if preferences.source != WaterTemperaturePreferencesSource.API and self.__api_errors_count < self.max_errors:
            LogsApiDataSource.log_warning("HeatingControl - UseCase: api error number: " + str(self.__api_errors_count))
            self.__api_errors_count += 1
        else:
            if self.__api_errors_count > 0:
                self.__api_errors_count -= 1
                LogsApiDataSource.log_info("HeatingControl - UseCase: api error number: " +
                                           str(self.__api_errors_count))

        if self.__api_errors_count == self.max_errors:
            LogsApiDataSource.log_error("HeatingControl - UseCase: api error number: " + str(self.__api_errors_count) +
                                        ". Creating local alert")
            self.__alerts_repository.create_local_alert(self.error_message)
            self.__api_errors_count = 0
