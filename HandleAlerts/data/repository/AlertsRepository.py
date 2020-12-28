import datetime

from HandleAlerts.data.datasource import ApiDataSource, LocalAlertsDataSource
from HandleAlerts.domain.model.Alert import Alert
from HandleAlerts.domain.model.DayOfWeek import DayOfWeek
from HandleAlerts.domain.model.StartingTime import StartingTime


class AlertsRepository:

    def ask_for_alerts(self):
        try:
            next_alert = ApiDataSource.get_alerts()
            self.__add_alert(next_alert)
            print("New alert Added")
        except Exception:
            pass

    def __add_alert(self, alert: Alert):
        if alert not in LocalAlertsDataSource.alerts:
            LocalAlertsDataSource.alerts.append(alert)
            print("Alert Added")

    def get_alerts(self):
        return LocalAlertsDataSource.alerts

    def create_local_alert(self, text):
        alert = Alert(StartingTime(DayOfWeek.MONDAY, 12, 0), text, datetime.datetime.now().timestamp())
        self.__add_alert(alert)
        print("New local alert")

