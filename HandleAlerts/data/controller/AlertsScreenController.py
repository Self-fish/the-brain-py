from Core.data.device import LCDStatus


class AlertsScreenController:

    def __init__(self, lcd):
        self.__lcd = lcd

    def show_alerts_advice(self):
        if LCDStatus.lcd_current_status != LCDStatus.LCDStatus.ALERTS_ADVICE_SCREEN:
            self.__lcd.lcd_load_custom_chars(self.main_font)
            self.__lcd.lcd_display_string("", 2, 2)
            self.__lcd.lcd_display_string("", 2, 3)
            self.__lcd.lcd_display_string("", 2, 4)
            self.__lcd.lcd_display_string("", 3, 2)
            self.__lcd.lcd_display_string("", 3, 3)
            self.__lcd.lcd_display_string("", 3, 4)
            self.__lcd.lcd_display_string("", 4, 2)
            self.__lcd.lcd_display_string("", 4, 3)
            self.__lcd.lcd_display_string("", 4, 4)
            self.__lcd.lcd_write_char_with_position(0, 2, 2)
            self.__lcd.lcd_write_char_with_position(1, 2, 3)
            self.__lcd.lcd_write_char_with_position(2, 2, 4)

            self.__lcd.lcd_write_char_with_position(3, 3, 2)
            self.__lcd.lcd_write_char_with_position(4, 3, 3)
            self.__lcd.lcd_write_char_with_position(3, 3, 4)

            self.__lcd.lcd_write_char_with_position(5, 4, 2)
            self.__lcd.lcd_write_char_with_position(1, 4, 3)
            self.__lcd.lcd_write_char_with_position(6, 4, 4)
            LCDStatus.lcd_current_status = LCDStatus.LCDStatus.ALERTS_ADVICE_SCREEN
