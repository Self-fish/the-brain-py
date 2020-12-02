
class WelcomeScreenController:

    welcome_font = [
        # Up Left cornet
        [0b11111,
         0b10000,
         0b10000,
         0b10000,
         0b10000,
         0b10000,
         0b10000,
         0b10000],
        # Down left corner
        [0b10000,
         0b10000,
         0b10000,
         0b10000,
         0b10000,
         0b10000,
         0b10000,
         0b11111],

        # Up right corner
        [0b11111,
         0b00001,
         0b00001,
         0b00001,
         0b00001,
         0b00001,
         0b00001,
         0b00001],

        # Down right corner
        [0b00001,
         0b00001,
         0b00001,
         0b00001,
         0b00001,
         0b00001,
         0b00001,
         0b11111],

        # Left side
        [0b10000,
         0b10000,
         0b10000,
         0b10000,
         0b10000,
         0b10000,
         0b10000,
         0b10000],

        # Right side
        [0b00001,
         0b00001,
         0b00001,
         0b00001,
         0b00001,
         0b00001,
         0b00001,
         0b00001],

        # Up side
        [0b11111,
         0b00000,
         0b00000,
         0b00000,
         0b00000,
         0b00000,
         0b00000,
         0b00000],

        # Down side
        [0b00000,
         0b00000,
         0b00000,
         0b00000,
         0b00000,
         0b00000,
         0b00000,
         0b11111]
    ]

    def __init__(self, lcd):
        self.__lcd = lcd
        self.__lcd.lcd_load_custom_chars(self.welcome_font)

    def build_frame(self):
        # Up frame
        self.__lcd.lcd_write_char_with_position(0, 1, 0)
        self.__lcd.lcd_write_char_with_position(6, 1, 1)
        self.__lcd.lcd_write_char_with_position(6, 1, 2)
        self.__lcd.lcd_write_char_with_position(6, 1, 3)
        self.__lcd.lcd_write_char_with_position(6, 1, 4)
        self.__lcd.lcd_write_char_with_position(6, 1, 5)
        self.__lcd.lcd_write_char_with_position(6, 1, 6)
        self.__lcd.lcd_write_char_with_position(6, 1, 7)
        self.__lcd.lcd_write_char_with_position(6, 1, 8)
        self.__lcd.lcd_write_char_with_position(6, 1, 9)
        self.__lcd.lcd_write_char_with_position(6, 1, 10)
        self.__lcd.lcd_write_char_with_position(6, 1, 11)
        self.__lcd.lcd_write_char_with_position(6, 1, 12)
        self.__lcd.lcd_write_char_with_position(6, 1, 13)
        self.__lcd.lcd_write_char_with_position(6, 1, 14)
        self.__lcd.lcd_write_char_with_position(6, 1, 15)
        self.__lcd.lcd_write_char_with_position(6, 1, 16)
        self.__lcd.lcd_write_char_with_position(6, 1, 17)
        self.__lcd.lcd_write_char_with_position(6, 1, 18)
        self.__lcd.lcd_write_char_with_position(2, 1, 19)
        # Right frame
        self.__lcd.lcd_write_char_with_position(5, 2, 19)
        self.__lcd.lcd_write_char_with_position(5, 3, 19)
        # Down frame
        self.__lcd.lcd_write_char_with_position(3, 4, 19)
        self.__lcd.lcd_write_char_with_position(7, 4, 18)
        self.__lcd.lcd_write_char_with_position(7, 4, 17)
        self.__lcd.lcd_write_char_with_position(7, 4, 16)
        self.__lcd.lcd_write_char_with_position(7, 4, 15)
        self.__lcd.lcd_write_char_with_position(7, 4, 14)
        self.__lcd.lcd_write_char_with_position(7, 4, 13)
        self.__lcd.lcd_write_char_with_position(7, 4, 12)
        self.__lcd.lcd_write_char_with_position(7, 4, 11)
        self.__lcd.lcd_write_char_with_position(7, 4, 10)
        self.__lcd.lcd_write_char_with_position(7, 4, 9)
        self.__lcd.lcd_write_char_with_position(7, 4, 8)
        self.__lcd.lcd_write_char_with_position(7, 4, 7)
        self.__lcd.lcd_write_char_with_position(7, 4, 6)
        self.__lcd.lcd_write_char_with_position(7, 4, 5)
        self.__lcd.lcd_write_char_with_position(7, 4, 4)
        self.__lcd.lcd_write_char_with_position(7, 4, 3)
        self.__lcd.lcd_write_char_with_position(7, 4, 2)
        self.__lcd.lcd_write_char_with_position(7, 4, 1)
        self.__lcd.lcd_write_char_with_position(1, 4, 0)
        # Left frame
        self.__lcd.lcd_write_char_with_position(4, 3, 0)
        self.__lcd.lcd_write_char_with_position(4, 2, 0)

    def write_user_message(self, user_name):
        self.__lcd.lcd_display_string("Hello " + user_name + "!", 2, 4)

    def write_version_message(self, version_code):
        self.__lcd.lcd_display_string("Version " + version_code , 3, 4)

    def write_initialising_message(self):
        self.__lcd.lcd_display_string("                  ", 3, 1)
        self.__lcd.lcd_display_string("Initialising...!", 3, 2)
