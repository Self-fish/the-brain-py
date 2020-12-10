from dependency_injector import containers, providers

from Core.data.driver import I2C_LCD_driver
from MainScreen.data.controller.LCDController import MainScreenController
from MeasureWaterTemp.data.repository.Repository import WaterTemperatureRepository


class MainScreenContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    lcd = providers.Singleton(I2C_LCD_driver.lcd)
    main_screen_controller = providers.Factory(MainScreenController, lcd)
    repository = providers.Singleton(WaterTemperatureRepository)
