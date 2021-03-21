from Core.data.driver.RelayController import RelayController
from Core.data.driver.RelayStatus import RelayStatus


class FillPumpRepository:

    def __init__(self, relay_controller: RelayController):
        self.__relay_controller = relay_controller
        self.__relay_controller.update_relay_status(RelayStatus.OFF)
        self.__pump_status = RelayStatus.OFF

    def switch_pump_off(self):
        print("Apagamos la bomba")
        if self.__pump_status != RelayStatus.OFF:
            self.__relay_controller.update_relay_status(RelayStatus.OFF)
            self.__pump_status = RelayStatus.OFF

    def switch_pump_on(self):
        print("Encendemos la bomba")
        if self.__pump_status != RelayStatus.ON:
            self.__relay_controller.update_relay_status(RelayStatus.ON)
            self.__pump_status = RelayStatus.ON
