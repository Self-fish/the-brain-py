from HandleAlerts.domain.model.DayOfWeek import DayOfWeek


class StartingTime:

    def __init__(self, day: DayOfWeek, hour, minute):
        self.__day = day
        self.__hour = hour
        self.__minute = minute

    def __eq__(self, other):
        if not isinstance(other, DayOfWeek):
            return False
        return self.__day == other.__day and self.__hour == other.__hour and self.__minute == other.__minute

    def get_day(self):
        return self.__day

    def get_hour(self):
        return self.__hour

    def get_minute(self):
        return self.__minute
