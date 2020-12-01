from WelcomeScreen.data import I2C_LCD_driver


def show_welcome_message():
    mylcd = I2C_LCD_driver.lcd()
    mylcd.lcd_display_string("Hello World!", 3, 4)
    print("Welcome Pablo!")
    print("Please Wait!")
