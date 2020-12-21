from enum import Enum


class LCDStatus(Enum):
    NONE = 0
    WELCOME_SCREEN = 1,
    MAIN_SCREEN = 2,
    ALERTS_ADVICE_SCREEN = 3


lcd_status = LCDStatus.NONE
