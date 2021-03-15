from Core.data.driver.RelayController import RelayController
from Core.data.driver.RelayStatus import RelayStatus


class FilterRepository:

    def __init__(self, filter_controller: RelayController):
        self.__filter_controller = filter_controller
        self.__filter_status = RelayStatus.ON

    def change_status(self, status: RelayStatus):
        if self.__filter_status != status:
            self.__filter_controller.update_relay_status(status)
            self.__filter_status = status
