from enum import Enum

from dependency_injector.wiring import Provide, inject

from Core.data.device.LCDStatus import LCDStatus
from HandleAlerts.HandleAlertsContainer import HandleAlertsContainer
from HandleAlerts.data.repository.AlertsRepository import AlertsRepository
from HandleMenu.domain.MenuOptions import MenuOptions
from MainScreen.MainScreenContainer import MainScreenContainer
from MainScreen.data.controller.LCDController import MainScreenController


class DisplayMenuUseCase:

    @inject
    def __init__(self, alerts_repository: AlertsRepository = Provide[HandleAlertsContainer.alerts_repository],
                 screen_controller: MainScreenController = Provide[MainScreenContainer.main_screen_controller]):
        self.__alerts_repository = alerts_repository
        self.__screen_controller = screen_controller
        self.__menu_options = [MenuOptions.SHOW_ALERTS, MenuOptions.LIGHT_CONTROL]

    def display_general_menu(self):
        LCDStatus.lcd_next_status = LCDStatus.LCDStatus.MENU
        if len(self.__alerts_repository.get_alerts()) == 0:
            self.__menu_options.remove(MenuOptions.SHOW_ALERTS)
        self.__screen_controller.print_menu(self.__menu_options, MenuOptions.LIGHT_CONTROL)
        self.__menu_options = [MenuOptions.SHOW_ALERTS, MenuOptions.LIGHT_CONTROL]
