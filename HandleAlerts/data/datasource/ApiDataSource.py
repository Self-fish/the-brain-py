import requests
import datetime

from requests.exceptions import ConnectionError, ConnectTimeout
from HandleAlerts.data.datasource.NoApiAlertsException import NoApiAlertsException
from HandleAlerts.domain.model.Alert import Alert
from HandleAlerts.domain.model.StartingTime import StartingTime

ALERTS_BASE_URL = "http://192.168.0.15:8082/alerts/"
NEXT_ALERT_PATH = "next"
EXECUTE_ALERT_PATH = "/execute"


def get_alerts():
    try:
        alerts = requests.get(ALERTS_BASE_URL + NEXT_ALERT_PATH)
        if alerts.status_code == 200:
            return Alert(alerts.json()['id'], StartingTime(alerts.json()['starts']['day'],
                                                           alerts.json()['starts']['hour'],
                                                           alerts.json()['starts']['minute']),
                         alerts.json()['text'], datetime.datetime.now().timestamp())
        elif alerts.status_code == 404:
            return None

        else:
            raise NoApiAlertsException

    except (ConnectionError, ConnectTimeout):
        raise NoApiAlertsException


def execute_alert(alert_id):
    try:
        response = requests.post(ALERTS_BASE_URL + alert_id + EXECUTE_ALERT_PATH)
        if response.status_code == 200:
            return True

        else:
            raise NoApiAlertsException

    except (ConnectionError, ConnectTimeout):
        raise NoApiAlertsException
