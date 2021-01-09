from dependency_injector.wiring import Provide, inject

from MainScreen.MainScreenContainer import MainScreenContainer
from MainScreen.data.controller import CurrentTimeController
from MainScreen.data.controller.LCDController import MainScreenController
from MainScreen.domain.model.MainScreenStep import MainScreenStep
from MeasureWaterTemp.data.datasource import LocalDataSource


class MainScreenUseCase:

    @inject
    def __init__(self, screen_controller: MainScreenController = Provide[MainScreenContainer.main_screen_controller]):
        self.__step = MainScreenStep.NONE
        self.__screen_controller = screen_controller

    def show_next_value(self):
        water_temperature = LocalDataSource.water_temperature
        self.__screen_controller.pain_template()
        self.__screen_controller.show_date(CurrentTimeController.get_current_hour())
        self.__screen_controller.show_temperature(water_temperature, self.__step)
        self.__step = MainScreenStep.WATER_TEMPERATURE

