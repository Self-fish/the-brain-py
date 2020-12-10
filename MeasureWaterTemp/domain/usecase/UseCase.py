from dependency_injector.wiring import Provide, inject

from MeasureWaterTemp.data.repository import Repository


class MeasureWaterTempUseCase:

    def track_water_temp(self):
        Repository.track_water_temp()

