from dependency_injector import containers, providers

from Core.data.driver.RelayController import RelayController
from HandleAlerts.data.repository.AlertsRepository import AlertsRepository
from HandleLights.data.repository.LightStatus import LightStatusRepository


class HandleLightsContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    light_controller = providers.Factory(RelayController, 0)
    light_status_repository = providers.Singleton(LightStatusRepository, light_controller)
