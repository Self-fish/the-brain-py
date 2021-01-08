import sys
import time

from dependency_injector.wiring import Provide, inject

from Core.data.device import LCDStatus
from Core.data.driver import JoystickController
from HandleAlerts.HandleAlertsContainer import HandleAlertsContainer
from HandleAlerts.data.repository.AlertsRepository import AlertsRepository
from HandleAlerts.domain.usecase.ShowAlerts import ShowAlerts
from HandleMenu.domain.MenuOptions import MenuOptions
from MainScreen.MainScreenContainer import MainScreenContainer
from MainScreen.data.controller.LCDController import MainScreenController


class DisplayMenuUseCase:

    handle_alerts_container = HandleAlertsContainer()
    handle_alerts_container.wire(modules=[sys.modules[__name__]])

    @inject
    def __init__(self, alerts_repository: AlertsRepository = Provide[HandleAlertsContainer.alerts_repository],
                 screen_controller: MainScreenController = Provide[MainScreenContainer.main_screen_controller]):
        self.__alerts_repository = alerts_repository
        self.__screen_controller = screen_controller
        self.__show_alerts_use_case = ShowAlerts()
        self.__menu_options = [MenuOptions.SHOW_ALERTS, MenuOptions.LIGHT_CONTROL]
        self.__selected_option = 0

    def display_general_menu(self):
        LCDStatus.lcd_next_status = LCDStatus.LCDStatus.MENU
        if len(self.__alerts_repository.get_alerts()) == 0:
            self.__menu_options.remove(MenuOptions.SHOW_ALERTS)
        self.__print_menu()
        time.sleep(1)
        self.__wait_joystick_interaction()
        self.__menu_options = [MenuOptions.SHOW_ALERTS, MenuOptions.LIGHT_CONTROL]
        self.__selected_option = 0


    def __wait_joystick_interaction(self):
        should_wait = True
        while should_wait:
            if JoystickController.is_joystick_down():
                if self.__selected_option != len(self.__menu_options) - 1:
                    self.__selected_option += 1
                    self.__print_menu()
                    time.sleep(1)
            elif JoystickController.is_joystick_up():
                if self.__selected_option != 0:
                    self.__selected_option -= 1
                    self.__print_menu()
                    time.sleep(1)
            elif JoystickController.is_switch_pressed():
                should_wait = False
                self.__select_option()

    def __print_menu(self):
        self.__screen_controller.print_menu(self.__menu_options, self.__menu_options[self.__selected_option])

    def __select_option(self):
        if self.__menu_options[self.__selected_option] == MenuOptions.SHOW_ALERTS:
            print(len(self.__alerts_repository.get_alerts()))
            print("Llamamos al show alerts use case")
            self.__show_alerts_use_case.display_alerts(0)
        else:
            LCDStatus.lcd_next_status = LCDStatus.LCDStatus.MAIN_SCREEN
