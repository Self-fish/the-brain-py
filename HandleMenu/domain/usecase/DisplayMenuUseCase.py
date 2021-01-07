from enum import Enum

from dependency_injector.wiring import Provide, inject

from HandleAlerts.HandleAlertsContainer import HandleAlertsContainer
from HandleAlerts.data.repository.AlertsRepository import AlertsRepository
from HandleMenu.domain.MenuOptions import MenuOptions


class DisplayMenuUseCase:

    @inject
    def __init__(self, alerts_repository: AlertsRepository = Provide[HandleAlertsContainer.alerts_repository]):
        self.__alerts_repository = alerts_repository
        self.__menu_options = [MenuOptions.SHOW_ALERTS, MenuOptions.LIGHT_CONTROL]

    def display_general_menu(self):
        if len(self.__alerts_repository.get_alerts()) == 0:
            self.__menu_options.remove(MenuOptions.SHOW_ALERTS)
        option: Enum = self.__menu_options[0]
        print(option.value)
        self.__menu_options = [MenuOptions.SHOW_ALERTS, MenuOptions.LIGHT_CONTROL]
