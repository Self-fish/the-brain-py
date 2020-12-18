from HandleAlerts.data.datasource import ApiDataSource


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

    def __add_alert(self, alert):
        if alert not in self.__alerts:
            self.__alerts.append(alert)
        print(len(self.__alerts))
        print(self.__alerts[0].__starting.__day)
        print(self.__alerts[0].__message)

    def get_local_alerts(self):
        print()