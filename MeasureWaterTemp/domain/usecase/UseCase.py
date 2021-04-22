from dependency_injector.wiring import Provide, inject

from Core.data.repository import NotificationsApiDataSource
from MeasureWaterTemp.MeasureWaterTempContainer import MeasureWaterTempContainer
from MeasureWaterTemp.data.repository.MeasureWaterRepository import MeasureWaterRepository


class MeasureWaterTempUseCase:

    max_error = 3
    error_message = "Measure Error"

    @inject
    def __init__(self, measure_water_repository: MeasureWaterRepository =
                 Provide[MeasureWaterTempContainer.measure_water_repository]):
        self.__measure_water_repository = measure_water_repository
        self.__api_errors_count = 0

    def track_water_temp(self):
        print("UseCase: track water temperature")
        request_success = self.__measure_water_repository.track_water_temp()
        self.__handle_possible_api_errors(request_success)

    def __handle_possible_api_errors(self, request_success: bool):
        if not request_success and self.__api_errors_count < self.max_error:
            self.__api_errors_count += 1
        else:
            if self.__api_errors_count > 0:
                self.__api_errors_count -= 1

        if self.__api_errors_count == self.max_error:
            NotificationsApiDataSource.create_notification("Something seems to be wrong while sending the current "
                                                           "water temperature.")
            self.__api_errors_count = 0
