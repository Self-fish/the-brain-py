import requests

from HandleAlerts.data.datasource.NoApiAlertsException import NoApiAlertsException
from HandleAlerts.domain.model.Alert import Alert

API_URI = "http://192.168.0.25:8082/alerts/next"


def get_alerts():
    alerts = requests.get(API_URI)
    if alerts.status_code != 200:
        raise NoApiAlertsException
    else:
        return Alert(alerts.json()['creationDate'], alerts.json()['text'])
