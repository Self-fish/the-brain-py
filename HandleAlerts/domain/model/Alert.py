

class Alert:

    def __init__(self, timestamp, message):
        self.__timestamp = timestamp
        self.__message = message

    def __eq__(self, other):
        if not isinstance(other, Alert):
            return False
        return self.__timestamp == other.__timestamp and self.__message == other.__message