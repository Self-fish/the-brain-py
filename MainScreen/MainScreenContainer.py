from dependency_injector import containers, providers

from Core.data.driver import I2C_LCD_driver
from MainScreen.data.controller.LCDController import MainScreenController


class MainScreenContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    lcd = providers.Singleton(I2C_LCD_driver.lcd)
    main_screen_controller = providers.Singleton(MainScreenController, lcd)
