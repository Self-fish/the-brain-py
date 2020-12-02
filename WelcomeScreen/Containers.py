from dependency_injector import providers, containers
from WelcomeScreen.data import I2C_LCD_driver
from WelcomeScreen.data.WelcomeScreenController import WelcomeScreenController


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    lcd = providers.Factory(I2C_LCD_driver.lcd)
    welcomeController = providers.Factory(WelcomeScreenController, lcd)

