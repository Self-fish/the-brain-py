from dependency_injector import containers, providers

from Core.data.driver.Controller import RelayController
from HeatingControl.data.repository.HeatingStatusRepository import HeatingStatusRepository


class HeatingControlContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    heating_controller = providers.Factory(RelayController, 2)
    heating_status_repository = providers.Singleton(HeatingStatusRepository, heating_controller)
