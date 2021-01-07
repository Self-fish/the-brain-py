from dependency_injector.wiring import Provide, inject

from Core.data.device import LCDStatus
from HandleAlerts.HandleAlertsContainer import HandleAlertsContainer
from HandleAlerts.data.repository.AlertsRepository import AlertsRepository


class ShowAlertsAdviseUseCase:

    @inject
    def __init__(self,
                 repository: AlertsRepository = Provide[HandleAlertsContainer.alerts_repository]):
        self.__repository = repository

    def show_alert_advice(self):
        if LCDStatus.lcd_next_status != LCDStatus.LCDStatus.SPECIFIC_ALERT and \
                len(self.__repository.get_alerts()) != 0:
            LCDStatus.lcd_next_status = LCDStatus.LCDStatus.ALERTS_ADVICE_SCREEN
