from dependency_injector.wiring import Provide, inject

from HandleAlerts.HandleAlertsContainer import HandleAlertsContainer
from HandleAlerts.data.repository.AlertsRepository import AlertsRepository


class ShowAlerts:

    @inject
    def __init__(self, repository: AlertsRepository = Provide[HandleAlertsContainer.alerts_repository]):
        self.__repository = repository

    def display_alerts(self):
        if self.__repository.get_alerts() != 0:
            print("Mostraríamos la alerta")
