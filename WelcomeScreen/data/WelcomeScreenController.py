from WelcomeScreen.data import I2C_LCD_driver


def show_welcome_message():
    mylcd = I2C_LCD_driver.lcd()
    mylcd.lcd_display_string("Hello Pablo!", 2, 4)
    mylcd.lcd_display_string("Initialising...", 3, 4)
