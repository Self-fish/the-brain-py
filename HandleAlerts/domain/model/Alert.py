from HandleAlerts.domain.model.StartingTime import StartingTime


class Alert:

    def __init__(self, starting: StartingTime, message, timestamp):
        self.__starting = starting
        self.__message = message
        self.__timestamp = timestamp

    def __eq__(self, other):
        if not isinstance(other, Alert):
            return False
        if self.__starting == other.__starting:
            print("Starting equal")

        return self.__starting == other.__starting and self.__message == other.__message

