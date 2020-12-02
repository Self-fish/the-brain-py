import sys

from dependency_injector.wiring import Provide, inject
from WelcomeScreen.Containers import Container
from WelcomeScreen.data import I2C_LCD_driver
from WelcomeScreen.data.WelcomeScreenController import WelcomeScreenController

container = Container()
container.wire(modules=[sys.modules[__name__]])

@inject
def show_screen(lcd: I2C_LCD_driver.lcd = Provide[Container.lcd]):
    controller = WelcomeScreenController(lcd)
    #controller.show_welcome_message()
    controller.test()
