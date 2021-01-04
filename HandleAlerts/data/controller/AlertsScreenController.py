

class AlertsScreenController:

    def __init__(self, lcd):
        self.__lcd = lcd

    def print_alert(self, date, text):
        self.__lcd.clear()
        self.__lcd.lcd_display_string(self, date, 1, 0)


