import time
import abc

from Core.data.device import LCDStatus
from Core.data.driver import JoystickController
from MainScreen.data.controller.LCDController import MainScreenController
from MainScreen.domain.usecase.UseCase import MainScreenUseCase


class MenuUseCase(abc.ABC):

    def __init__(self, screen_controller: MainScreenController):
        self.__screen_controller = screen_controller
        self.menu_options = None
        self.selected_option = 0
        self.main_Screen_use_case: MainScreenUseCase = None

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

    def display_error_message(self, error_message):
        self.__screen_controller.print_error_message(error_message)

    def __print_menu(self):
        self.__screen_controller.print_menu(self.menu_options, self.menu_options[self.selected_option])

    def finish_menu(self):
        LCDStatus.lcd_next_status = LCDStatus.LCDStatus.MAIN_SCREEN
        self.main_Screen_use_case.show_next_value()



