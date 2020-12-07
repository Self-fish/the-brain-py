from MainScreen.data.controller import DHTController, DS18B20Controller
from MainScreen.domain.model.MainScreenStep import MainScreenStep


class MainScreenUseCase:

    def __init__(self):
        self.__step = MainScreenStep.NONE

    def show_next_value(self):
        DS18B20Controller.read_temperature()
