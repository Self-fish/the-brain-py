from enum import Enum


class LCDStatus(Enum):
    NONE = 0
    WELCOME_SCREEN = 1,
    MAIN_SCREEN = 2,
    ALERTS_ADVICE_SCREEN = 3,
    SPECIFIC_ALERT = 4


lcd_current_status = LCDStatus.NONE
lcd_next_status = LCDStatus.MAIN_SCREEN
