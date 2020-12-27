from dependency_injector import containers, providers

from Core.data.driver.RelayController import RelayController
from Core.data.net.NetworkController import NetworkController
from HandleAlerts.data.repository.GetAlertsRepository import GetAlertsRepository
from HandleLights.data.datasource.ApiDataSource import ApiDataSource
from HandleLights.data.repository.LightStatus import LightStatusRepository
from HandleLights.data.repository.Preferences import PreferencesRepository


class HandleLightsContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    light_controller = providers.Factory(RelayController, 0)
    alerts_repository = providers.Singleton(GetAlertsRepository)
    network_controller = providers.Singleton(NetworkController, alerts_repository)
    api_datasource = providers.Factory(ApiDataSource, network_controller)
    light_status_repository = providers.Singleton(LightStatusRepository, light_controller)
    preferences_repository = providers.Factory(PreferencesRepository, api_datasource)
