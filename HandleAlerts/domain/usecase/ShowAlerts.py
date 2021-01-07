import time
from datetime import datetime

from dependency_injector.wiring import Provide, inject
from pytz import timezone

from Core.data.device import LCDStatus
from Core.data.driver import JoystickController
from HandleAlerts.HandleAlertsContainer import HandleAlertsContainer
from HandleAlerts.data.repository.AlertsRepository import AlertsRepository
from HandleAlerts.domain.model.Alert import Alert
from MainScreen.MainScreenContainer import MainScreenContainer
from MainScreen.data.controller.LCDController import MainScreenController


class ShowAlerts:

    @inject
    def __init__(self, repository: AlertsRepository = Provide[HandleAlertsContainer.alerts_repository],
                 screen_controller: MainScreenController = Provide[MainScreenContainer.main_screen_controller]):
        self.__repository = repository
        self.__screen_controller = screen_controller

    def display_alerts(self, position):
        print("total alerts: " + str(len(self.__repository.get_alerts())))
        print("Position: " + str(position))
        if len(self.__repository.get_alerts()) != 0:
            if self.__there_are_still_more_alerts(position):
                print("Alerts to show")
                LCDStatus.lcd_next_status = LCDStatus.LCDStatus.SPECIFIC_ALERT
                self.__print_alert(position)
                time.sleep(1)
                self.__handle_joystick_movements_when_alert_displayed(position)
            else:
                print("No alerts to show")
        #        self.__screen_controller.print_alerts_complete()
        #        self.__handle_joystick_movements_when_finish(position)

    def __print_alert(self, position):
        alert: Alert = self.__repository.get_alerts()[position]
        date = datetime.fromtimestamp(alert.timestamp, timezone('Europe/Madrid')).strftime("%H:%M  %d %b %Y")
        self.__screen_controller.print_alert(date, alert.message)

    def __there_are_still_more_alerts(self, position):
        return position + 1 <= len(self.__repository.get_alerts())

    def __handle_joystick_movements_when_alert_displayed(self, position):
        while True:
            if JoystickController.is_joystick_right():
                self.display_alerts(position + 1)
            elif position != 0 and JoystickController.is_joystick_left():
                self.display_alerts(position - 1)
            time.sleep(1)

    def __handle_joystick_movements_when_finish(self, position):
        should_wait = True
        while should_wait:
            if JoystickController.is_switch_pressed():
                should_wait = False
                self.__repository.reset_alerts()
                LCDStatus.lcd_next_status = LCDStatus.LCDStatus.MAIN_SCREEN
            elif position != 0 and JoystickController.is_joystick_left():
                self.display_alerts(position - 1)
            time.sleep(1)
