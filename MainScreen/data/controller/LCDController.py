from Core.data.device import LCDStatus
from MainScreen.domain.model.MainScreenStep import MainScreenStep


class MainScreenController:

    anchor_font = [
        # Anchor
        [0b00000,
         0b00000,
         0b00100,
         0b01110,
         0b01010,
         0b01110,
         0b00100,
         0b00100],

        # Anchor
        [0b00000,
         0b00000,
         0b11111,
         0b00000,
         0b00000,
         0b00000,
         0b00000,
         0b00000],

        # Anchor
        [0b00100,
         0b00100,
         0b11111,
         0b00100,
         0b00100,
         0b00100,
         0b00100,
         0b00100],

        # Anchor
        [0b00100,
         0b00100,
         0b00100,
         0b00100,
         0b00100,
         0b00100,
         0b00100,
         0b11111],

        # Anchor
        [0b00000,
         0b00000,
         0b11110,
         0b11100,
         0b11100,
         0b10010,
         0b00001,
         0b00000],

        # Anchor
        [0b00000,
         0b00000,
         0b01111,
         0b00111,
         0b00111,
         0b01001,
         0b10000,
         0b00000],

        [0b00000,
         0b00000,
         0b00000,
         0b00000,
         0b00000,
         0b00000,
         0b00000,
         0b00000],

        # Water temperature icon
        [0b00100,
         0b01010,
         0b01010,
         0b01110,
         0b01110,
         0b11111,
         0b11111,
         0b01110],
    ]

    def __init__(self, lcd):
        self.__lcd = lcd

    def pain_template(self):
        if LCDStatus.lcd_next_status == LCDStatus.LCDStatus.MAIN_SCREEN and \
                LCDStatus.lcd_current_status != LCDStatus.LCDStatus.MAIN_SCREEN:
            self.__lcd.lcd_load_custom_chars(self.anchor_font)
            self.__lcd.lcd_clear()
            self.__paint_anchor_icon()
            LCDStatus.lcd_current_status = LCDStatus.LCDStatus.MAIN_SCREEN

    def show_date(self, date):
        if LCDStatus.lcd_current_status == LCDStatus.LCDStatus.MAIN_SCREEN or \
                LCDStatus.lcd_next_status == LCDStatus.LCDStatus.MAIN_SCREEN:
            self.__lcd.lcd_display_string(date, 1, 1)

    def show_temperature(self, temperature, current_step: MainScreenStep):
        if LCDStatus.lcd_current_status == LCDStatus.LCDStatus.MAIN_SCREEN:
            if current_step != MainScreenStep.WATER_TEMPERATURE:
                self.__lcd.lcd_write_char_with_position(7, 3, 9)
            self.__lcd.lcd_display_string(str(temperature) + " C", 3, 11)

    def __paint_anchor_icon(self):
        self.__lcd.lcd_write_char_with_position(0, 2, 3)
        self.__lcd.lcd_write_char_with_position(1, 3, 2)
        self.__lcd.lcd_write_char_with_position(1, 3, 4)
        self.__lcd.lcd_write_char_with_position(2, 3, 3)
        self.__lcd.lcd_write_char_with_position(3, 4, 3)
        self.__lcd.lcd_write_char_with_position(4, 4, 2)
        self.__lcd.lcd_write_char_with_position(5, 4, 4)


