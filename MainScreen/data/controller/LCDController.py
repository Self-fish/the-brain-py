

class MainScreenController:

    main_font = [
        # Up Left cornet
        [0b00000,
         0b00000,
         0b00100,
         0b01110,
         0b01010,
         0b01110,
         0b00100,
         0b00100],

        # Down left corner
        [0b00000,
         0b00000,
         0b11111,
         0b00000,
         0b00000,
         0b00000,
         0b00000,
         0b00000],

        # Up right corner
        [0b00100,
         0b00100,
         0b11111,
         0b00100,
         0b00100,
         0b00100,
         0b00100,
         0b00100],

        # Down right corner
        [0b00100,
         0b00100,
         0b00100,
         0b00100,
         0b00100,
         0b00100,
         0b00100,
         0b11111],

        # Left side
        [0b00000,
         0b00000,
         0b11110,
         0b11100,
         0b11100,
         0b10010,
         0b00001,
         0b00000],

        # Right side
        [0b00000,
         0b00000,
         0b01111,
         0b00111,
         0b00111,
         0b01001,
         0b10000,
         0b00000],

        # Up side
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
        self.__lcd.lcd_load_custom_chars(self.main_font)

    def pain_template(self):
        self.__lcd.lcd_write_char_with_position(0, 2, 3)
        self.__lcd.lcd_write_char_with_position(1, 3, 2)
        self.__lcd.lcd_write_char_with_position(1, 3, 4)
        self.__lcd.lcd_write_char_with_position(2, 3, 3)
        self.__lcd.lcd_write_char_with_position(3, 4, 3)
        self.__lcd.lcd_write_char_with_position(4, 4, 2)
        self.__lcd.lcd_write_char_with_position(5, 4, 4)

    def show_temperature(self, temperature):
        self.__lcd.lcd_clear()
        self.__lcd.lcd_display_string("Temperature " + str(temperature) + " C", 3, 4)
