from dependency_injector import containers, providers

from HandleAlerts.data.repository.AlertsRepository import AlertsRepository


class HandleAlertsContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    alerts_repository = providers.Singleton(AlertsRepository)
