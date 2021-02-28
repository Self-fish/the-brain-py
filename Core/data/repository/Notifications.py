from pip._vendor import requests

API_URI = "http://192.168.0.15:8085/notifications/"


def create_notification(message):
    try:
        body = message
        response = requests.post(API_URI, json=body)
        print(response.status_code)
    except Exception:
        print("Oh nooo!")
        pass