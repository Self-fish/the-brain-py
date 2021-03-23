from dependency_injector.wiring import inject, Provide

from Core.data.driver.RelayStatus import RelayStatus
from Core.data.repository import LogsApiDataSource, NotificationsApiDataSource
from HeaterControl.HeaterControlContainer import HeaterControlContainer
from HeaterControl.data.repository import WaterTemperatureRepository
from HeaterControl.data.repository.HeaterStatusRepository import HeaterStatusRepository
from HeaterControl.domain.model.WaterTemperaturePreferences import WaterTemperaturePreferences
from HeaterControl.domain.model.WaterTemperaturePreferencesSource import WaterTemperaturePreferencesSource
from MeasureWaterTemp.data.datasource import LocalDataSource


class HeaterControlUseCase:

    max_errors = 3
    error_message = "Temp Preference Error"

    @inject
    def __init__(self, heater_status_repository:
                 HeaterStatusRepository = Provide[HeaterControlContainer.heater_status_repository]):
        self.__heater_status_repository = heater_status_repository
        self.__api_errors_count = 0

    def control_heating(self):
        LogsApiDataSource.log_info("HeaterControl - UseCase: comparing if water temperature fits requirements")
        desired_water_temperature: WaterTemperaturePreferences = WaterTemperatureRepository.get_heating_temperature()
        LogsApiDataSource.log_info("HeaterControl - UseCase: "
                                   "the desired temperature is " + str(desired_water_temperature.temperature))
        current_water_temperature = LocalDataSource.water_temperature
        LogsApiDataSource.log_info("HeaterControl - UseCase: "
                                   "the current temperature is " + str(current_water_temperature))
        if current_water_temperature < (desired_water_temperature.temperature + 0.1):
            self.__heater_status_repository.update_heater_status(RelayStatus.ON, current_water_temperature)
        else:
            self.__heater_status_repository.update_heater_status(RelayStatus.OFF, current_water_temperature)
        self.__handle_possible_api_errors(desired_water_temperature)

    def switch_off_heater_and_block(self):
        self.__heater_status_repository.turn_off_heater_and_block()

    def unblock_heaters(self):
        self.__heater_status_repository.unblock_heaters()

    def __handle_possible_api_errors(self, preferences: WaterTemperaturePreferences):
        if preferences.source != WaterTemperaturePreferencesSource.API and self.__api_errors_count < self.max_errors:
            LogsApiDataSource.log_warning("HeaterControl - UseCase: api error number: " + str(self.__api_errors_count))
            self.__api_errors_count += 1
        else:
            if self.__api_errors_count > 0:
                self.__api_errors_count -= 1
                LogsApiDataSource.log_info("HeaterControl - UseCase: api error number: " +
                                           str(self.__api_errors_count))

        if self.__api_errors_count == self.max_errors:
            LogsApiDataSource.log_error("HeaterControl - UseCase: api error number: " + str(self.__api_errors_count) +
                                        ". Creating remote notification")
            NotificationsApiDataSource.create_notification("Something seems to be wrong with the remote preferences."
                                                           "Impossible to get the desired water temperature")
            self.__api_errors_count = 0
