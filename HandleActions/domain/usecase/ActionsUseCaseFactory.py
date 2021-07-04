import sys

from EmptyAquariumAction.EmptyAquariumActionContainer import EmptyAquariumActionContainer
from EmptyAquariumAction.domain.usecase.EmptyAquariumUseCase import EmptyAquariumUseCase
from FillAquariumAction.FillAquariumActionContainer import FillAquariumActionContainer
from FillAquariumAction.domain.usecase.FillAquariumUseCase import FillAquariumUseCase
from HandleActions.domain.model.Action import Action
from HandleLights.domain.usecase.UseCase import HandleLightsUseCase
from HeaterControl.domain.usecase import UseCase

empty_aquarium_container = EmptyAquariumActionContainer()
empty_aquarium_container.wire(modules=[sys.modules[__name__]])
fill_aquarium_container = FillAquariumActionContainer()
fill_aquarium_container.wire(modules=[sys.modules[__name__]])


def build_use_case(action: Action, general_heater_use_case: UseCase, lights_use_case: HandleLightsUseCase):
    if action.step == "EMPTY_AQUARIUM":
        empty_aquarium_use_case = EmptyAquariumUseCase()
        empty_aquarium_use_case.lazy_injection(general_heater_use_case, lights_use_case)
        return empty_aquarium_use_case
    elif action.step == "FILL_AQUARIUM":
        fill_aquarium_use_case = FillAquariumUseCase()
        fill_aquarium_use_case.lazy_injection(general_heater_use_case, lights_use_case)
        return fill_aquarium_use_case

