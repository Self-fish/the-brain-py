from dependency_injector import containers, providers

from HandleAlerts.data.repository.GetAlertsRepository import GetAlertsRepository


class HandleAlertsContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    alerts_repository_repository = providers.Singleton(GetAlertsRepository)