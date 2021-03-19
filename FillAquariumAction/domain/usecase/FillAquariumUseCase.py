import time
from dependency_injector.wiring import inject, Provide

from Core.data.driver.DS18B20Controller import DS18B20Controller
from Core.domain.usecases.CoreActionUseCase import CoreActionUseCase
from FillAquariumAction.FillAquariumActionContainer import FillAquariumActionContainer


class FillAquariumUseCase(CoreActionUseCase):

    @inject
    def __init__(self, water_temperature_controller: DS18B20Controller = Provide[FillAquariumActionContainer.
                 water_temperature_controller]):
        self.__water_temperature_controller: DS18B20Controller = water_temperature_controller

    def execute_action(self):
        while True:
            print(self.__water_temperature_controller.read_device_temperature())
            time.sleep(5)
