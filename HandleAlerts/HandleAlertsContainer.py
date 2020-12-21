from dependency_injector import containers, providers

from Core.data.driver import I2C_LCD_driver
from HandleAlerts.data.controller.AlertsScreenController import AlertsScreenController
from HandleAlerts.data.repository.GetAlertsRepository import GetAlertsRepository


class HandleAlertsContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    alerts_repository_repository = providers.Singleton(GetAlertsRepository)
    lcd = providers.Singleton(I2C_LCD_driver.lcd)
    alerts_screen_controller = providers.Factory(AlertsScreenController, lcd)
