from Core.domain.usecases.CoreActionUseCase import CoreActionUseCase
from HandleActions.domain.model.Action import Action


class EmptyAquariumUseCase(CoreActionUseCase):

    def execute_action(self):
        print("Vaciamos el aquario!")
