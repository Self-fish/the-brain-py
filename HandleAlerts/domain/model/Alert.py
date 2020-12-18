from HandleAlerts.domain.model.StartingTime import StartingTime


class Alert:

    def __init__(self, starting: StartingTime, message):
        self.__starting = starting
        self.__message = message

    def __eq__(self, other):
        if not isinstance(other, Alert):
            return False
        return self.__starting == other.__starting and self.__message == other.__message
