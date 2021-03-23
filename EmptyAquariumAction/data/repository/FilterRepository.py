from Core.data.driver.RelayController import RelayController
from Core.data.driver.RelayStatus import RelayStatus


class FilterRepository:

    def __init__(self, filter_controller: RelayController):
        self.__filter_controller = filter_controller
        self.__filter_status = RelayStatus.OFF

    def switch_filter_off(self):
        if self.__filter_status != RelayStatus.ON:
            self.__filter_controller.update_relay_status(RelayStatus.ON)
            self.__filter_status = RelayStatus.ON

    def switch_filter_on(self):
        if self.__filter_status != RelayStatus.OFF:
            self.__filter_controller.update_relay_status(RelayStatus.OFF)
            self.__filter_status = RelayStatus.OFF
