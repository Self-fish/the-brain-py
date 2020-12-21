from dependency_injector.wiring import Provide, inject

from HandleAlerts.HandleAlertsContainer import HandleAlertsContainer
from HandleAlerts.data.repository.GetAlertsRepository import GetAlertsRepository


class ShowAlertsAdviseUseCase:

    @inject
    def __init__(self, repository: GetAlertsRepository = Provide[HandleAlertsContainer.alerts_repository_repository]):
        self.__repository = repository

    def show_alert_advice(self):
        if len(self.__repository.get_local_alerts()) != 0:
            print("Mostraríamos el warning")