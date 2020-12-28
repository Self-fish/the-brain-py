import requests
import datetime

from requests.exceptions import ConnectionError, ConnectTimeout
from HandleAlerts.data.datasource.NoApiAlertsException import NoApiAlertsException
from HandleAlerts.domain.model.Alert import Alert
from HandleAlerts.domain.model.StartingTime import StartingTime

API_URI = "http://192.168.0.25:8082/alerts/next"


def get_alerts():
    try:
        alerts = requests.get(API_URI)
        if alerts.status_code == 200:
            return Alert(StartingTime(alerts.json()['starts']['day'], alerts.json()['starts']['hour'],
                                      alerts.json()['starts']['minute']),
                         alerts.json()['text'], datetime.datetime.now().timestamp())
        elif alerts.status_code == 404:
            return None

        else:
            raise NoApiAlertsException

    except (ConnectionError, ConnectTimeout):
        raise NoApiAlertsException
