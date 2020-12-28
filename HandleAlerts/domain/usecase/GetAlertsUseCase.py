from dependency_injector.wiring import Provide, inject

from HandleAlerts.HandleAlertsContainer import HandleAlertsContainer
from HandleAlerts.data.repository.AlertsRepository import AlertsRepository


class GetAlertsUseCase:

    @inject
    def __init__(self, repository: AlertsRepository = Provide[HandleAlertsContainer.alerts_repository]):
        self.__repository = repository

    def get_alerts(self):
        self.__repository.ask_for_alerts()
