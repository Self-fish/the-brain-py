from Core.data.driver.Controller import RelayController


class HeatingStatusRepository:

    def __init__(self, heating_controller: RelayController):
        self.__heating_controller = heating_controller
        self.__current_heating_status = self.__heating_controller.get_current_relay_status()

    def update_heating_status(self, heating_status):
        if heating_status != self.__current_heating_status:
            self.__heating_controller.update_relay_status(heating_status)
            self.__current_heating_status = heating_status
