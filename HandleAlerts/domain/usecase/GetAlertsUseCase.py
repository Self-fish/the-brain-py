from dependency_injector.wiring import Provide, inject

from HandleAlerts.HandleAlertsContainer import HandleAlertsContainer
from HandleAlerts.data.repository.AlertsRepository import AlertsRepository


class GetAlertsUseCase:

    @inject
    def __init__(self, repository: AlertsRepository = Provide[HandleAlertsContainer.alerts_repository]):
        self.__repository = repository
        self.__api_errors_count = 0

    def get_alerts(self):
        request_success = self.__repository.ask_for_alerts()
        self.__handle_possible_api_errors(request_success)

    def __handle_possible_api_errors(self, request_success: bool):
        if not request_success and self.__api_errors_count < 3:
            self.__api_errors_count += 1
        else:
            if self.__api_errors_count > 0:
                self.__api_errors_count -= 1

        if self.__api_errors_count == 10:
            self.__repository.create_local_alert("Remote Alerts Error")
            self.__api_errors_count = 0
