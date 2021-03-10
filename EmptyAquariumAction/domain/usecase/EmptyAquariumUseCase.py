from Core.domain.usecases.CoreActionUseCase import CoreActionUseCase
from EmptyAquariumAction.data.controller import MCP3008Controller


class EmptyAquariumUseCase(CoreActionUseCase):

    def execute_action(self):
        i = 0
        while i < 10:
            distance = MCP3008Controller.calculate_distance()
            print(distance)
            i = i + 1

