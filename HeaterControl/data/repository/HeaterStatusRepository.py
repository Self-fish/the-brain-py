from Core.data.driver.RelayController import RelayController
from Core.data.driver.RelayStatus import RelayStatus
from Core.data.logs import LogsApiDataSource
from HeaterControl.domain.model.ActiveHeater import ActiveHeater


class HeaterStatusRepository:

    max_retries = 1

    def __init__(self, first_heater_controller: RelayController, second_heater_controller: RelayController):
        self.__first_heater_controller = first_heater_controller
        self.__second_heater_controller = second_heater_controller
        self.__heater_active: ActiveHeater = ActiveHeater.NONE
        self.__number_of_tries = 0
        self.__previous_temperature = 0
        self.__turn_off_heaters()

    def __turn_off_heaters(self):
        self.__manage_first_heater(RelayStatus.OFF)
        self.__manage_second_heater(RelayStatus.OFF)

    def update_heating_status(self, heater_status, current_temperature):
        if heater_status == RelayStatus.ON and current_temperature is not 0:
            if self.__heater_active == ActiveHeater.NONE:
                self.__activate_heaters(current_temperature)

            elif self.__previous_temperature == current_temperature:
                if self.__number_of_tries < self.max_retries:
                    self.__number_of_tries += 1
                else:
                    self.__activate_heaters(current_temperature)

            elif self.__previous_temperature > current_temperature:
                self.__activate_heaters(current_temperature)

            elif self.__previous_temperature < current_temperature:
                self.__previous_temperature = current_temperature

        else:
            self.__deactivate_heaters()

    def __manage_first_heater(self, relay_status):
        self.__first_heater_controller.update_relay_status(relay_status)

    def __manage_second_heater(self, relay_status):
        self.__second_heater_controller.update_relay_status(relay_status)

    def __activate_heaters(self, current_temperature):
        if self.__heater_active == ActiveHeater.NONE:
            self.__manage_first_heater(RelayStatus.ON)
            self.__heater_active = ActiveHeater.FIRST_HEATER
            LogsApiDataSource.log_info("HeaterControl - HeaterStatusRepository: "
                                       "Heater 1 set to ON")
            LogsApiDataSource.log_info("HeaterControl - HeaterStatusRepository: "
                                       "Heater 2 set to OFF")
        elif self.__heater_active == ActiveHeater.FIRST_HEATER:
            self.__manage_first_heater(RelayStatus.OFF)
            self.__manage_second_heater(RelayStatus.ON)
            self.__heater_active = ActiveHeater.SECOND_HEATER
            LogsApiDataSource.log_info("HeaterControl - HeaterStatusRepository: "
                                       "Heater 1 set to OFF")
            LogsApiDataSource.log_info("HeaterControl - HeaterStatusRepository: "
                                       "Heater 2 set to ON")
        elif self.__heater_active == ActiveHeater.SECOND_HEATER:
            self.__manage_first_heater(RelayStatus.ON)
            self.__manage_second_heater(RelayStatus.ON)
            self.__heater_active = ActiveHeater.BOTH
            LogsApiDataSource.log_info("HeaterControl - HeaterStatusRepository: "
                                       "Heater 1 set to ON")
            LogsApiDataSource.log_info("HeaterControl - HeaterStatusRepository: "
                                       "Heater 2 set to ON")
        self.__previous_temperature = current_temperature
        self.__number_of_tries = 0

    def __deactivate_heaters(self):
        if self.__heater_active == ActiveHeater.FIRST_HEATER:
            self.__manage_first_heater(RelayStatus.OFF)
            self.__manage_second_heater(RelayStatus.OFF)
            self.__heater_active = ActiveHeater.NONE
            LogsApiDataSource.log_info("HeaterControl - HeaterStatusRepository: "
                                       "Heater 1 set to OFF")
            LogsApiDataSource.log_info("HeaterControl - HeaterStatusRepository: "
                                       "Heater 2 set to OFF")
        elif self.__heater_active == ActiveHeater.SECOND_HEATER:
            self.__manage_first_heater(RelayStatus.ON)
            self.__manage_second_heater(RelayStatus.OFF)
            self.__heater_active = ActiveHeater.FIRST_HEATER
            LogsApiDataSource.log_info("HeaterControl - HeaterStatusRepository: "
                                       "Heater 1 set to ON")
            LogsApiDataSource.log_info("HeaterControl - HeaterStatusRepository: "
                                       "Heater 2 set to OFF")
        elif self.__heater_active == ActiveHeater.BOTH:
            self.__manage_first_heater(RelayStatus.OFF)
            self.__manage_second_heater(RelayStatus.ON)
            self.__heater_active = ActiveHeater.SECOND_HEATER
            LogsApiDataSource.log_info("HeaterControl - HeaterStatusRepository: "
                                       "Heater 1 set to OFF")
            LogsApiDataSource.log_info("HeaterControl - HeaterStatusRepository: "
                                       "Heater 2 set to ON")
        self.__number_of_tries = 0


