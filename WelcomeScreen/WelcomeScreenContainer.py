from dependency_injector import providers, containers
from Core.data import I2C_LCD_driver
from WelcomeScreen.data.controller.LCDController import WelcomeScreenController


class WelcomeContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    lcd = providers.Singleton(I2C_LCD_driver.lcd)
    welcomeController = providers.Factory(WelcomeScreenController, lcd)

