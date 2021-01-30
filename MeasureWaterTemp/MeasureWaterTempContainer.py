from dependency_injector import containers, providers

from MeasureWaterTemp.data.repository.MeasureWaterRepository import MeasureWaterRepository


class MeasureWaterTempContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    measure_water_repository = providers.Singleton(MeasureWaterRepository)
