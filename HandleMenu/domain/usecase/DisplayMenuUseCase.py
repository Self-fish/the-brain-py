import time

from dependency_injector.wiring import Provide, inject

from Core.data.device import LCDStatus
from Core.data.driver import JoystickController
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
        self.__selected_option = 0

    def display_general_menu(self):
        LCDStatus.lcd_next_status = LCDStatus.LCDStatus.MENU
        if len(self.__alerts_repository.get_alerts()) == 0:
            self.__menu_options.remove(MenuOptions.SHOW_ALERTS)
        self.__screen_controller.print_menu(self.__menu_options, self.__menu_options[0])
        self.__wait_joystick_interaction()
        self.__menu_options = [MenuOptions.SHOW_ALERTS, MenuOptions.LIGHT_CONTROL]


    def __wait_joystick_interaction(self):
        should_wait = True
        while should_wait:
            if JoystickController.is_joystick_down():
                if self.__selected_option != len(self.__menu_options) - 1:
                    print("Joystick Down")
                    self.__selected_option += 1
                    print(self.__selected_option)
                    time.sleep(1)
            elif JoystickController.is_joystick_up():
                if self.__selected_option != 0:
                    print("Joystic Up")
                    self.__selected_option -= 1
                    print(self.__selected_option)
                    time.sleep(1)
            elif JoystickController.is_switch_pressed():
                LCDStatus.lcd_next_status = LCDStatus.LCDStatus.MAIN_SCREEN
                should_wait = False
