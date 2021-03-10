from EmptyAquariumAction.domain.usecase.EmptyAquariumUseCase import EmptyAquariumUseCase
from HandleActions.domain.model.Action import Action


def build_use_case(action: Action):
    if action.step == "EMPTY_AQUARIUM":
        return EmptyAquariumUseCase()
