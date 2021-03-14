from Core.domain.usecases.CoreActionUseCase import CoreActionUseCase
from EmptyAquariumAction.data.controller import MCP3008Controller


class EmptyAquariumUseCase(CoreActionUseCase):

    def execute_action(self):
        distance = MCP3008Controller.calculate_distance()
        print(distance)
