import datetime

from HandleAlerts.data.datasource import ApiDataSource
from HandleAlerts.data.datasource.NoApiAlertsException import NoApiAlertsException
from HandleAlerts.domain.model.Alert import Alert
from HandleAlerts.domain.model.DayOfWeek import DayOfWeek
from HandleAlerts.domain.model.StartingTime import StartingTime


class AlertsRepository:

    def __init__(self):
        self.__alerts = []

    def ask_for_alerts(self):
        try:
            next_alert = ApiDataSource.get_alerts()
            if next_alert is not None:
                self.__add_alert(next_alert)
                return next_alert.alert_id
            else:
                return 0

        except NoApiAlertsException:
            return -1

    def execute_alert(self, alert_id):
        try:
            ApiDataSource.execute_alert(alert_id)
            return True
        except NoApiAlertsException:
            return False

    def __add_alert(self, alert: Alert):
        if alert not in self.__alerts:
            self.__alerts.append(alert)

    def get_alerts(self):
        return self.__alerts

    def create_local_alert(self, text):
        alert = Alert("-1", StartingTime(DayOfWeek.MONDAY, 12, 0), text, datetime.datetime.now().timestamp())
        self.__add_alert(alert)

    def reset_alerts(self):
        self.__alerts = []

