import sys

from HandleLights.domain.usecase.UseCase import HandleLightsUseCase
from WelcomeScreen.WelcomeScreenContainer import Container
from WelcomeScreen.domain.usecase.UseCase import WelcomeScreenUseCase

if __name__ == '__main__':
    container = Container()
    container.wire(modules=[sys.modules[__name__]])
    useCase = WelcomeScreenUseCase()
    useCase.show_screen()
    light_use_case = HandleLightsUseCase()
    light_use_case.handle_lights()

