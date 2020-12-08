from enum import Enum


class MainScreenStep(Enum):
    NONE = 0,
    BOX_TEMPERATURE = 1,
    BOX_HUMIDITY = 2,
    WATER_TEMPERATURE = 3
