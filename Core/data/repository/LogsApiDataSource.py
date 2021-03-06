import requests

from Core.data.repository.LogLevel import LogLevel

LOGS_URL = "http://192.168.0.15:8084/logs/"


def __post_log(log_level: LogLevel, message):
    try:
        body = {"severity": log_level.name, "message": message}
        requests.post(LOGS_URL, json=body)
    except Exception:
        pass


def log_info(message):
    __post_log(LogLevel.INFO, message)


def log_warning(message):
    __post_log(LogLevel.WARNING, message)


def log_error(message):
    __post_log(LogLevel.SEVERE, message)
