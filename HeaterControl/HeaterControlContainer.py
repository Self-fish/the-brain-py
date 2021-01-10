from dependency_injector import containers, providers

from Core.data.driver.RelayController import RelayController
from HeaterControl.data.repository.HeaterStatusRepository import HeaterStatusRepository


class HeaterControlContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    first_heater_controller = providers.Factory(RelayController, 2)
    second_heater_controller = providers.Factory(RelayController, 4)
    heater_status_repository = providers.Singleton(HeaterStatusRepository,
                                                   first_heater_controller,
                                                   second_heater_controller)
