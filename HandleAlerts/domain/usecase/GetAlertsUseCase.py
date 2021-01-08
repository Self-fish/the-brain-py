from dependency_injector.wiring import Provide, inject

from HandleAlerts.HandleAlertsContainer import HandleAlertsContainer
from HandleAlerts.data.repository.AlertsRepository import AlertsRepository


class GetAlertsUseCase:

    max_errors = 10
    error_message = "Remote Alerts Error"

    @inject
    def __init__(self, repository: AlertsRepository = Provide[HandleAlertsContainer.alerts_repository]):
        print("Creamos GetAlertsUseCase")
        self.__repository = repository
        self.__api_errors_count = 0

    def get_alerts(self):
        alert_id = self.__repository.ask_for_alerts()
        if alert_id != -1 and alert_id != 0:
            self.__handle_possible_api_errors(True)
            executed_success = self.__repository.execute_alert(alert_id)
            self.__handle_possible_api_errors(executed_success)
        elif alert_id == -1:
            self.__handle_possible_api_errors(False)

    def __handle_possible_api_errors(self, request_success: bool):
        if not request_success and self.__api_errors_count < 3:
            self.__api_errors_count += 1
        else:
            if self.__api_errors_count > 0:
                self.__api_errors_count -= 1

        if self.__api_errors_count == self.max_errors:
            self.__repository.create_local_alert(self.error_message)
            self.__api_errors_count = 0
