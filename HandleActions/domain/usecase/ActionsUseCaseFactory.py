import sys

from EmptyAquariumAction.EmptyAquariumActionContainer import EmptyAquariumActionContainer
from EmptyAquariumAction.domain.usecase.EmptyAquariumUseCase import EmptyAquariumUseCase
from FillAquariumAction.FillAquariumActionContainer import FillAquariumActionContainer
from FillAquariumAction.domain.usecase.FillAquariumUseCase import FillAquariumUseCase
from HandleActions.domain.model.Action import Action


empty_aquarium_container = EmptyAquariumActionContainer()
empty_aquarium_container.wire(modules=[sys.modules[__name__]])
fill_aquarium_container = FillAquariumActionContainer()
fill_aquarium_container.wire(modules=[sys.modules[__name__]])


def build_use_case(action: Action):
    if action.step == "EMPTY_AQUARIUM":
        return EmptyAquariumUseCase()
    elif action.step == "FILL_AQUARIUM":
        return FillAquariumUseCase()

