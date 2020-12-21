from dependency_injector.wiring import Provide, inject

from HandleAlerts.HandleAlertsContainer import HandleAlertsContainer
from HandleAlerts.data.controller.AlertsScreenController import AlertsScreenController
from HandleAlerts.data.repository.GetAlertsRepository import GetAlertsRepository


class ShowAlertsAdviseUseCase:

    @inject
    def __init__(self,
                 repository: GetAlertsRepository = Provide[HandleAlertsContainer.alerts_repository_repository],
                 screen_controller: AlertsScreenController = Provide[HandleAlertsContainer.alerts_screen_controller]):
        self.__repository = repository
        self.__screen_controller = screen_controller

    def show_alert_advice(self):
        if len(self.__repository.get_local_alerts()) != 0:
            print("Mostraríamos el warning")
            self.__screen_controller.show_alerts_advice()