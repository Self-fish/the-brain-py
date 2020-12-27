import requests

from Core.data.net import NoApiException
from HandleAlerts.data.repository.GetAlertsRepository import GetAlertsRepository

API_URI = "http://192.168.0.25:8080/"


class NetworkController:

    def __init__(self, alerts_repository: GetAlertsRepository):
        self.__alerts_repository = alerts_repository
        self.__errors_amount = 0

    def get_request(self, query_params):
        print("Get request")
        try:
            current_request = requests.get(API_URI + query_params)
        except Exception:
            print("Network controller exception")
        if current_request.status_code == 500:
            print("Error 500")
            if self.__errors_amount < 3:
                print("Network controller: Incrementamos")
                self.__errors_amount += 1
            else:
                self.__alerts_repository.create_local_alert()
                raise NoApiException
        else:
            print("Estamos en el else")
            if self.__errors_amount != 0:
                print("Network controller: decrementamos")
                self.__errors_amount -= 1
            return current_request
