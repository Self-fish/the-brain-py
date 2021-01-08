from dependency_injector.wiring import Provide, inject

from HandleAlerts.HandleAlertsContainer import HandleAlertsContainer
from HandleAlerts.data.repository.AlertsRepository import AlertsRepository
from MeasureWaterTemp.data.repository import Repository


class MeasureWaterTempUseCase:

    max_error = 10
    error_message = "Measure Error"

    def __init__(self, alerts_repository: AlertsRepository = Provide[HandleAlertsContainer.alerts_repository]):
        self.__alerts_repository = alerts_repository
        self.__api_errors_count = 0

    def track_water_temp(self):
        request_success = Repository.track_water_temp()
        self.__handle_possible_api_errors(request_success)

    def __handle_possible_api_errors(self, request_success: bool):
        if not request_success and self.__api_errors_count < 3:
            self.__api_errors_count += 1
        else:
            if self.__api_errors_count > 0:
                self.__api_errors_count -= 1

        if self.__api_errors_count == self.max_error:
            self.__alerts_repository.create_local_alert(self.error_message)
            self.__api_errors_count = 0
