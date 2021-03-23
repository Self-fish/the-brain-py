import sys

from EmptyAquariumAction.EmptyAquariumActionContainer import EmptyAquariumActionContainer
from EmptyAquariumAction.domain.usecase.EmptyAquariumUseCase import EmptyAquariumUseCase
from FillAquariumAction.FillAquariumActionContainer import FillAquariumActionContainer
from FillAquariumAction.domain.usecase.FillAquariumUseCase import FillAquariumUseCase
from HandleActions.domain.model.Action import Action
from HandleLights.HandleLightsContainer import HandleLightsContainer
from HeaterControl.domain.usecase import UseCase
from TurnOffLight.domain.usecase.TurnOffLightUseCase import TurnOffLightUseCase

empty_aquarium_container = EmptyAquariumActionContainer()
empty_aquarium_container.wire(modules=[sys.modules[__name__]])
fill_aquarium_container = FillAquariumActionContainer()
fill_aquarium_container.wire(modules=[sys.modules[__name__]])
handle_light_container = HandleLightsContainer()
handle_light_container.wire(modules=[sys.modules[__name__]])


def build_use_case(action: Action, general_heater_use_case: UseCase):
    if action.step == "EMPTY_AQUARIUM":
        empty_aquarium_use_case = EmptyAquariumUseCase()
        empty_aquarium_use_case.lazy_injection(general_heater_use_case)
        return empty_aquarium_use_case
    elif action.step == "FILL_AQUARIUM":
        return FillAquariumUseCase()
    elif action.step == "TURN_OFF_LIGHT":
        return TurnOffLightUseCase()

