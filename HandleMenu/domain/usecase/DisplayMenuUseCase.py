from dependency_injector.wiring import Provide, inject

from HandleAlerts.HandleAlertsContainer import HandleAlertsContainer
from HandleAlerts.data.repository.AlertsRepository import AlertsRepository
from HandleMenu.domain.MenuOptions import MenuOptions


class DisplayMenuUseCase:

    @inject
    def __init__(self, alerts_repository: AlertsRepository = Provide[HandleAlertsContainer.alerts_repository]):
        self.__alerts_repository = alerts_repository
        self.__menu_options = [MenuOptions.LIGHT_CONTROL]

    def display_menu(self):
        if len(self.__alerts_repository.get_alerts()) != 0:
            self.__menu_options.insert(0, MenuOptions.SHOW_ALERTS)
        for option in self.__menu_options:
            print(option)
