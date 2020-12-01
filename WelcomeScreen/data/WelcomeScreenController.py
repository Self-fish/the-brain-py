from WelcomeScreen.data import I2C_LCD_driver

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


def show_welcome_message():
    mylcd = I2C_LCD_driver.lcd()
    mylcd.lcd_load_custom_chars(welcome_font)
    mylcd.lcd_write_char_with_position(0, 1, 0)
    mylcd.lcd_write_char_with_position(6, 1, 1)
    mylcd.lcd_write_char_with_position(6, 1, 2)
    mylcd.lcd_write_char_with_position(6, 1, 3)
    mylcd.lcd_write_char_with_position(6, 1, 4)
    mylcd.lcd_write_char_with_position(6, 1, 5)
    mylcd.lcd_write_char_with_position(6, 1, 6)
    mylcd.lcd_write_char_with_position(6, 1, 7)
    mylcd.lcd_write_char_with_position(6, 1, 8)
    mylcd.lcd_write_char_with_position(6, 1, 9)
    mylcd.lcd_write_char_with_position(6, 1, 10)
    mylcd.lcd_write_char_with_position(6, 1, 11)
    mylcd.lcd_write_char_with_position(6, 1, 12)
    mylcd.lcd_write_char_with_position(6, 1, 13)
    mylcd.lcd_write_char_with_position(6, 1, 14)
    mylcd.lcd_write_char_with_position(6, 1, 15)
    mylcd.lcd_write_char_with_position(6, 1, 16)
    mylcd.lcd_write_char_with_position(6, 1, 17)
    mylcd.lcd_write_char_with_position(6, 1, 18)
    mylcd.lcd_write_char_with_position(6, 1, 19)
    mylcd.lcd_display_string("Hello Pablo!", 2, 4)
    mylcd.lcd_display_string("Initialising...!", 3, 2)
