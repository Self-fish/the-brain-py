from dependency_injector.wiring import Provide, inject

from MeasureWaterTemp.MeasureWaterTempContainer import MeasureWaterTempContainer
from MeasureWaterTemp.data.repository.Repository import WaterTemperatureRepository


class MeasureWaterTempUseCase:

    @inject
    def __init__(self, repository: WaterTemperatureRepository = Provide[MeasureWaterTempContainer.repository]):
        self.__repository = repository

    def track_water_temp(self):
        self.__repository.track_water_temp()

