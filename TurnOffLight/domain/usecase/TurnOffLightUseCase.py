from dependency_injector.wiring import inject, Provide

from Core.data.driver.RelayStatus import RelayStatus
from Core.domain.usecases.CoreActionUseCase import CoreActionUseCase
from HandleLights.HandleLightsContainer import HandleLightsContainer
from HandleLights.data.repository.LightStatus import LightStatusRepository


class TurnOffLightUseCase(CoreActionUseCase):

    @inject
    def __init__(self, light_status_repository: LightStatusRepository = Provide[HandleLightsContainer.
                 light_status_repository]):
        self.__light_status_repository = light_status_repository

    def execute_action(self):
        self.__light_status_repository.update_light_status(RelayStatus.OFF)
