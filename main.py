import sys

from dependency_injector.wiring import inject, Provide

from WelcomeScreen.Containers import Container
from WelcomeScreen.data import I2C_LCD_driver
from WelcomeScreen.data.WelcomeScreenController import WelcomeScreenController
from WelcomeScreen.domain import WelcomeScreenUseCase


@inject
def show_screen(lcd: I2C_LCD_driver.lcd = Provide[Container.lcd]):
    controller = WelcomeScreenController(lcd)
    #controller.show_welcome_message()
    controller.test()


if __name__ == '__main__':
    container = Container()
    container.wire(modules=[sys.modules[__name__]])
    show_screen()

