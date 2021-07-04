from dependency_injector import containers, providers

from Core.data.driver.DS18B20Controller import DS18B20Controller
from Core.data.driver.RelayController import RelayController
from FillAquariumAction.data.repository.FillPumpRepository import FillPumpRepository


class FillAquariumActionContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    water_temperature_controller = providers.Factory(DS18B20Controller, '28-00000b1106c6')
    fill_pump_controller = providers.Factory(RelayController, 26)
    fill_pump_repository = providers.Singleton(FillPumpRepository, fill_pump_controller)

