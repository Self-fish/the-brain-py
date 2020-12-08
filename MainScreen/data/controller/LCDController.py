

class MainScreenController:

    def __init__(self, lcd):
        self.__lcd = lcd

    def show_temperature(self, temperature):
        self.__lcd.lcd_clear()
        self.__lcd.lcd_display_string("Temperature " + str(temperature) + " ºC", 3, 4)
