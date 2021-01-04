from dependency_injector import containers, providers

from Core.data.driver import I2C_LCD_driver
from HandleAlerts.data.controller.AlertsScreenController import AlertsScreenController
from HandleAlerts.data.repository.AlertsRepository import AlertsRepository
from MainScreen.MainScreenContainer import MainScreenContainer


class HandleAlertsContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    alerts_repository = providers.Singleton(AlertsRepository)
    alerts_screen_controller = providers.Factory(AlertsScreenController, MainScreenContainer.lcd)
