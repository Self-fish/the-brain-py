from dependency_injector.wiring import inject, Provide

from Core.data.driver.RelayStatus import RelayStatus
from Core.domain.usecases.CoreActionUseCase import CoreActionUseCase
from EmptyAquariumAction.EmptyAquariumActionContainer import EmptyAquariumActionContainer
from EmptyAquariumAction.data.controller import MCP3008Controller
from EmptyAquariumAction.data.repository.FilterRepository import FilterRepository


class EmptyAquariumUseCase(CoreActionUseCase):

    @inject
    def __init__(self, filter_repository: FilterRepository = Provide[EmptyAquariumActionContainer.filter_repository]):
        self.__filter_repository = filter_repository

    def execute_action(self):
        # 1. Encender el calendator del cubo de llenado
        # 2. Parar el Filtro
        # 3. Empezar a vaciar hasta el valor que toque
        # 4. Parar el calentador del cubo de llenado

        self.__filter_repository.change_status(RelayStatus.OFF)



        while True:
            distance = MCP3008Controller.calculate_distance()
            print(distance)
