from dependency_injector.wiring import inject, Provide

from Core.data.driver.RelayStatus import RelayStatus
from HandleAlerts.HandleAlertsContainer import HandleAlertsContainer
from HandleAlerts.data.repository.AlertsRepository import AlertsRepository
from HeaterControl.HeaterControlContainer import HeaterControlContainer
from HeaterControl.data.repository import WaterTemperatureRepository
from HeaterControl.data.repository.HeaterStatusRepository import HeaterStatusRepository
from HeaterControl.domain.model.WaterTemperaturePreferences import WaterTemperaturePreferences
from HeaterControl.domain.model.WaterTemperaturePreferencesSource import WaterTemperaturePreferencesSource
from MeasureWaterTemp.data.datasource import LocalDataSource


class HeaterControlUseCase:

    max_errors = 10
    error_message = "Temp Preference Error"

    @inject
    def __init__(self, heater_status_repository:
                 HeaterStatusRepository = Provide[HeaterControlContainer.heater_status_repository],
                 alerts_repository: AlertsRepository = Provide[HandleAlertsContainer.alerts_repository]):
        self.__heater_status_repository = heater_status_repository
        self.__alerts_repository = alerts_repository
        self.__api_errors_count = 0

    def control_heating(self):
        desired_water_temperature: WaterTemperaturePreferences = WaterTemperatureRepository.get_heating_temperature()
        current_water_temperature = LocalDataSource.water_temperature
        if current_water_temperature < (desired_water_temperature.temperature + 0.1):
            self.__heater_status_repository.update_heating_status(RelayStatus.ON, current_water_temperature)
        else:
            self.__heater_status_repository.update_heating_status(RelayStatus.OFF, current_water_temperature)
        self.__handle_possible_api_errors(desired_water_temperature)

    def __handle_possible_api_errors(self, preferences: WaterTemperaturePreferences):
        if preferences.source != WaterTemperaturePreferencesSource.API and self.__api_errors_count < 3:
            self.__api_errors_count += 1
        else:
            if self.__api_errors_count > 0:
                self.__api_errors_count -= 1

        if self.__api_errors_count == self.max_errors:
            self.__alerts_repository.create_local_alert(self.error_message)
            self.__api_errors_count = 0
