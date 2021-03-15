from Core.data.driver.RelayController import RelayController
from Core.data.driver.RelayStatus import RelayStatus


class EmptyPumpRepository:

    def __init__(self, relay_controller: RelayController):
        self.__relay_controller = relay_controller
        self.__pump_status = RelayStatus.OFF

    def switch_pump_off(self):
        if self.__pump_status != RelayStatus.OFF:
            self.__relay_controller.update_relay_status(RelayStatus.OFF)
            self.__pump_status = RelayStatus.OFF

    def switch_pump_on(self):
        if self.__pump_status != RelayStatus.ON:
            self.__relay_controller.update_relay_status(RelayStatus.ON)
            self.__pump_status = RelayStatus.ON
