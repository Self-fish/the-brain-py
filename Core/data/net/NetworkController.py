import requests

from Core.data.net import NoApiException

API_URI = "http://192.168.0.25:8080/"


def get_request(query_params):

    current_request = requests.get(API_URI + query_params)
    if current_request.status_code != 200:
        print("NetworkController: No API")
        raise NoApiException
    else:
        return current_request.json()