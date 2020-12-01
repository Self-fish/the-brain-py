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
    mylcd.lcd_write_char(0, 1, 0)
    mylcd.lcd_display_string("Hello Pablo!", 2, 4)
    mylcd.lcd_display_string("Initialising...!", 3, 2)
