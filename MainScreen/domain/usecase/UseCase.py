from dependency_injector.wiring import Provide, inject

from MainScreen.MainScreenContainer import MainScreenContainer
from MainScreen.data.controller import CurrentTimeController
from MeasureWaterTemp.data.controller import DS18B20Controller
from MainScreen.data.controller.LCDController import MainScreenController
from MainScreen.domain.model.MainScreenStep import MainScreenStep
from MeasureWaterTemp.data.repository.Repository import WaterTemperatureRepository


class MainScreenUseCase:

    @inject
    def __init__(self, screen_controller: MainScreenController = Provide[MainScreenContainer.main_screen_controller],
                 water_temp_repository: WaterTemperatureRepository = Provide[MainScreenContainer.repository]):
        self.__step = MainScreenStep.NONE
        self.__screen_controller = screen_controller
        self.__water_temp_repository = water_temp_repository

    def show_next_value(self):
        water_temperature = DS18B20Controller.read_temperature()
        #water_temperature = self.__water_temp_repository.get_water_temp()
        self.__screen_controller.show_date(CurrentTimeController.get_current_hour())
        self.__screen_controller.pain_template()
        self.__screen_controller.show_temperature(water_temperature, self.__step)
        self.__step = MainScreenStep.WATER_TEMPERATURE

