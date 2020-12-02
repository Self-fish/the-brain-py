from dependency_injector.wiring import inject


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

    @inject
    def __init__(self, lcd):
        self.lcd = lcd
        self.lcd.lcd_load_custom_chars(self.welcome_font)

    def __build_frame(self):
        # Up frame
        self.lcd.lcd_write_char_with_position(0, 1, 0)
        self.lcd.lcd_write_char_with_position(6, 1, 1)
        self.lcd.lcd_write_char_with_position(6, 1, 2)
        self.lcd.lcd_write_char_with_position(6, 1, 3)
        self.lcd.lcd_write_char_with_position(6, 1, 4)
        self.lcd.lcd_write_char_with_position(6, 1, 5)
        self.lcd.lcd_write_char_with_position(6, 1, 6)
        self.lcd.lcd_write_char_with_position(6, 1, 7)
        self.lcd.lcd_write_char_with_position(6, 1, 8)
        self.lcd.lcd_write_char_with_position(6, 1, 9)
        self.lcd.lcd_write_char_with_position(6, 1, 10)
        self.lcd.lcd_write_char_with_position(6, 1, 11)
        self.lcd.lcd_write_char_with_position(6, 1, 12)
        self.lcd.lcd_write_char_with_position(6, 1, 13)
        self.lcd.lcd_write_char_with_position(6, 1, 14)
        self.lcd.lcd_write_char_with_position(6, 1, 15)
        self.lcd.lcd_write_char_with_position(6, 1, 16)
        self.lcd.lcd_write_char_with_position(6, 1, 17)
        self.lcd.lcd_write_char_with_position(6, 1, 18)
        self.lcd.lcd_write_char_with_position(2, 1, 19)
        # Right frame
        self.lcd.lcd_write_char_with_position(5, 2, 19)
        self.lcd.lcd_write_char_with_position(5, 3, 19)
        # Down frame
        self.lcd.lcd_write_char_with_position(3, 4, 19)
        self.lcd.lcd_write_char_with_position(7, 4, 18)
        self.lcd.lcd_write_char_with_position(7, 4, 17)
        self.lcd.lcd_write_char_with_position(7, 4, 16)
        self.lcd.lcd_write_char_with_position(7, 4, 15)
        self.lcd.lcd_write_char_with_position(7, 4, 14)
        self.lcd.lcd_write_char_with_position(7, 4, 13)
        self.lcd.lcd_write_char_with_position(7, 4, 12)
        self.lcd.lcd_write_char_with_position(7, 4, 11)
        self.lcd.lcd_write_char_with_position(7, 4, 10)
        self.lcd.lcd_write_char_with_position(7, 4, 9)
        self.lcd.lcd_write_char_with_position(7, 4, 8)
        self.lcd.lcd_write_char_with_position(7, 4, 7)
        self.lcd.lcd_write_char_with_position(7, 4, 6)
        self.lcd.lcd_write_char_with_position(7, 4, 5)
        self.lcd.lcd_write_char_with_position(7, 4, 4)
        self.lcd.lcd_write_char_with_position(7, 4, 3)
        self.lcd.lcd_write_char_with_position(7, 4, 2)
        self.lcd.lcd_write_char_with_position(7, 4, 1)
        self.lcd.lcd_write_char_with_position(1, 4, 0)
        # Left frame
        self.lcd.lcd_write_char_with_position(4, 3, 0)
        self.lcd.lcd_write_char_with_position(4, 2, 0)

    def __write_message(self):
        self.lcd.lcd_display_string("Hello Pablo!", 2, 4)
        self.lcd.lcd_display_string("Initialising...!", 3, 2)

    def show_welcome_message(self):
        self.__build_frame()
        self.__write_message()

    def test(self):
        print("Hola")
        print(self.lcd)
