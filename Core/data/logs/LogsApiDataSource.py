import requests

from Core.data.logs.LogLevel import LogLevel

LOGS_URL = "http://192.168.0.25:8084/logs/"


def __post_log(log_level: LogLevel, message):
    body = {"severity": log_level.name, "message": message}
    print(body)
    requests.post(LOGS_URL, json=body)


def log_info(message):
    __post_log(LogLevel.INFO, message)


def log_warning(message):
    __post_log(LogLevel.WARNING, message)


def log_error(message):
    __post_log(LogLevel.SEVERE, message)
