import time
from datetime import datetime

from dependency_injector.wiring import Provide, inject
from pytz import timezone

from Core.data.device import LCDStatus
from Core.data.driver import JoystickDriver
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
        if len(self.__repository.get_alerts()) != 0 :
            if position + 1 <= len(self.__repository.get_alerts()):
                LCDStatus.lcd_next_status = LCDStatus.LCDStatus.SPECIFIC_ALERT
                alert: Alert = self.__repository.get_alerts()[0]
                date = datetime.fromtimestamp(alert.timestamp, timezone('Europe/Madrid')).strftime("%H:%M  %d %b %Y")
                self.__screen_controller.print_alert(date, alert.message)
                while True:
                    if JoystickDriver.is_joystick_right():
                        self.display_alerts(position + 1)
                    time.sleep(1)
            else:
                print("Ya no hay más alertas que mostrar")
                self.__repository.reset_alerts()
                LCDStatus.lcd_next_status = LCDStatus.LCDStatus.MAIN_SCREEN

