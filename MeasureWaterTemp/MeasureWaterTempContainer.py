from dependency_injector import containers, providers

from Core.data.driver.DS18B20Controller import DS18B20Controller
from MeasureWaterTemp.data.repository.MeasureWaterRepository import MeasureWaterRepository


class MeasureWaterTempContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    water_temperature_controller = providers.Factory(DS18B20Controller, '28-00000b10eb34')
    measure_water_repository = providers.Singleton(MeasureWaterRepository, water_temperature_controller)
