import sys

from dependency_injector.wiring import inject, Provide

from WelcomeScreen.Containers import Container
from WelcomeScreen.data import I2C_LCD_driver
from WelcomeScreen.data.WelcomeScreenController import WelcomeScreenController
from WelcomeScreen.domain import WelcomeScreenUseCase


if __name__ == '__main__':
    container = Container()
    container.wire(modules=[sys.modules[__name__]])
    useCase = WelcomeScreenUseCase()
    useCase.show_screen()

