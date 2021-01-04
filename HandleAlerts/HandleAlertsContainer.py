from dependency_injector import containers, providers

from Core.data.driver import I2C_LCD_driver
from HandleAlerts.data.controller.AlertsScreenController import AlertsScreenController
from HandleAlerts.data.repository.AlertsRepository import AlertsRepository


class HandleAlertsContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    alerts_repository = providers.Singleton(AlertsRepository)
    lcd = providers.Singleton(I2C_LCD_driver.lcd)
    alerts_screen_controller = providers.Factory(AlertsScreenController, lcd)
