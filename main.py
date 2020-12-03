import sys

from HandleLights.domain.usecase.UseCase import HandleLightsUseCase
from WelcomeScreen.WelcomeScreenContainer import WelcomeContainer
from HandleLights.HandleLightsContainer import HandleLightsContainer
from WelcomeScreen.domain.usecase.UseCase import WelcomeScreenUseCase

if __name__ == '__main__':
    welcome_container = WelcomeContainer()
    welcome_container.wire(modules=[sys.modules[__name__]])
    handle_lights_container = HandleLightsContainer()
    handle_lights_container.wire(modules=[sys.modules[__name__]])
    welcome_screen_use_case = WelcomeScreenUseCase()
    welcome_screen_use_case.show_screen()
    handle_light_use_case = HandleLightsUseCase()
    handle_light_use_case.handle_lights()

