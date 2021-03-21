from dependency_injector import containers, providers

from Core.data.driver.RelayController import RelayController
from EmptyAquariumAction.data.repository.EmptyPumpRepository import EmptyPumpRepository
from EmptyAquariumAction.data.repository.FillWaterHeaterRepository import FillWaterHeaterRepository
from EmptyAquariumAction.data.repository.FilterRepository import FilterRepository


class EmptyAquariumActionContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    filter_controller = providers.Factory(RelayController, 1)
    empty_pump_controller = providers.Factory(RelayController, 5)
    fill_water_heater_controller = providers.Factory(RelayController, 6)
    filter_repository = providers.Singleton(FilterRepository, filter_controller)
    empty_pump_repository = providers.Singleton(EmptyPumpRepository, empty_pump_controller)
    fill_water_heater_repository = providers.Singleton(FillWaterHeaterRepository, fill_water_heater_controller)
