from dependency_injector import containers, providers

from HandleLights.data.controller.Controller import LightsController
from HandleLights.data.repository.LightStatus import LightStatusRepository


class HandleLightsContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    light_controller = providers.Singleton(LightsController)
    light_status_repository = providers.Singleton(LightStatusRepository, light_controller)
