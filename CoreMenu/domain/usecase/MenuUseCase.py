import time
import abc

from dependency_injector.wiring import Provide, inject

from Core.data.device import LCDStatus
from Core.data.driver import JoystickController
from MainScreen.MainScreenContainer import MainScreenContainer
from MainScreen.data.controller.LCDController import MainScreenController


class MenuUseCase(abc.ABC):

    @inject
    def __init__(self, screen_controller: MainScreenController = Provide[MainScreenContainer.main_screen_controller]):
        self.__screen_controller = screen_controller
        self.menu_options = None
        self.selected_option = 0

    @abc.abstractmethod
    def build_menu_options(self):
        pass

    @abc.abstractmethod
    def select_option(self):
        pass

    def display_menu(self):
        LCDStatus.lcd_next_status = LCDStatus.LCDStatus.MENU
        self.build_menu_options()
        self.__print_menu()
        time.sleep(1)
        self.__wait_joystick_interaction()
        self.menu_options = None
        self.selected_option = 0

    def __wait_joystick_interaction(self):
        should_wait = True
        while should_wait:
            if JoystickController.is_joystick_down():
                if self.selected_option != len(self.menu_options) - 1:
                    self.selected_option += 1
                    self.__print_menu()
                    time.sleep(1)
            elif JoystickController.is_joystick_up():
                if self.selected_option != 0:
                    self.selected_option -= 1
                    self.__print_menu()
                    time.sleep(1)
            elif JoystickController.is_switch_pressed():
                should_wait = False
                self.select_option()

    def __print_menu(self):
        self.__screen_controller.print_test()
        self.__screen_controller.print_menu(self.menu_options, self.menu_options[self.selected_option])

