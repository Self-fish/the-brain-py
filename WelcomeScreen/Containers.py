from dependency_injector import providers, containers
from WelcomeScreen.data import I2C_LCD_driver


class Container(containers.DeclarativeContainer):

    lcd = providers.Singleton(I2C_LCD_driver.lcd)

