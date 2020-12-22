from dependency_injector.wiring import Provide, inject

from Core.data.device import LCDStatus
from HandleAlerts.HandleAlertsContainer import HandleAlertsContainer
from HandleAlerts.data.repository.GetAlertsRepository import GetAlertsRepository


class ShowAlertsAdviseUseCase:

    @inject
    def __init__(self,
                 repository: GetAlertsRepository = Provide[HandleAlertsContainer.alerts_repository_repository]):
        self.__repository = repository
        #self.__screen_controller = screen_controller

    def show_alert_advice(self):
        if len(self.__repository.get_local_alerts()) != 0:
            print("Mostraríamos el warning")
            LCDStatus.lcd_status = LCDStatus.LCDStatus.ALERTS_ADVICE_SCREEN
            #self.__screen_controller.show_alerts_advice()