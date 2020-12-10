from dependency_injector import containers, providers

from MeasureWaterTemp.data.repository.Repository import WaterTemperatureRepository


class MeasureWaterTempContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    repository = providers.Singleton(WaterTemperatureRepository)
