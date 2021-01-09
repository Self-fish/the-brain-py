from dependency_injector import containers, providers

from Core.data.driver.RelayController import RelayController
from HeatingControl.data.repository.HeatingStatusRepository import HeatingStatusRepository


class HeatingControlContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    first_heating_controller = providers.Factory(RelayController, 2)
    second_heating_controller = providers.Factory(RelayController, 50)
    heating_status_repository = providers.Singleton(HeatingStatusRepository,
                                                    first_heating_controller,
                                                    second_heating_controller)
