from HandleAlerts.data.datasource import ApiDataSource
from HandleAlerts.domain.model.Alert import Alert


class GetAlertsRepository:

    def __init__(self):
        self.__alerts = []

    def ask_for_alerts(self):
        try:
            next_alert = ApiDataSource.get_alerts()
            self.__add_alert(next_alert)
        except Exception:
            print("Exception")
            pass

    def __add_alert(self, alert: Alert):
        if alert not in self.__alerts:
            self.__alerts.append(alert)
        print(len(self.__alerts))
        first: Alert = self.__alerts[0]
        print(first.get_starting().get_day())
        print(first.get_starting().get_hour())
        print(first.get_starting().get_minute())
        print(first.get_message())

    def get_local_alerts(self):
        print()