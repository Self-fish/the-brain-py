import time
from dependency_injector.wiring import inject, Provide

from Core.data.driver.DS18B20Controller import DS18B20Controller
from Core.domain.usecases.CoreActionUseCase import CoreActionUseCase
from EmptyAquariumAction.EmptyAquariumActionContainer import EmptyAquariumActionContainer
from EmptyAquariumAction.data.controller import MCP3008Controller
from EmptyAquariumAction.data.repository.FillWaterHeaterRepository import FillWaterHeaterRepository
from EmptyAquariumAction.data.repository.FilterRepository import FilterRepository
from FillAquariumAction.FillAquariumActionContainer import FillAquariumActionContainer
from FillAquariumAction.data.repository.FillPumpRepository import FillPumpRepository
from HeaterControl.HeaterControlContainer import HeaterControlContainer
from HeaterControl.data.repository.HeaterStatusRepository import HeaterStatusRepository
from HeaterControl.domain.usecase import UseCase


class FillAquariumUseCase(CoreActionUseCase):

    @inject
    def __init__(self, water_temperature_controller: DS18B20Controller = Provide[FillAquariumActionContainer.
                 water_temperature_controller],
                 fill_water_heater_repository: FillWaterHeaterRepository =
                 Provide[EmptyAquariumActionContainer.fill_water_heater_repository],
                 fill_pump_repository: FillPumpRepository =
                 Provide[FillAquariumActionContainer.fill_pump_repository],
                 filter_repository: FilterRepository =
                 Provide[EmptyAquariumActionContainer.filter_repository]):
        self.__water_temperature_controller: DS18B20Controller = water_temperature_controller
        self.__fill_water_heater_repository = fill_water_heater_repository
        self.__fill_pump_repository = fill_pump_repository
        self.__filter_repository = filter_repository
        self.__general_heater_use_case: UseCase = None

    def lazy_injection(self, general_heater_use_case: UseCase):
        self.__general_heater_use_case = general_heater_use_case

    def execute_action(self):
        self.__fill_pump_repository.switch_pump_off()
        self.__heat_water()
        original_distance = MCP3008Controller.calculate_distance()
        print("Original didtance: " + str(original_distance))
        distance = 99
        self.__fill_pump_repository.switch_pump_on()
        while distance > original_distance - 4:
            distance = MCP3008Controller.calculate_distance()
            print(distance)
            if distance < 6:
                break
        self.__fill_pump_repository.switch_pump_off()
        if distance < 6:
            self.__filter_repository.switch_filter_on()
            self.__general_heater_use_case.unblock_heaters()

    def __heat_water(self):
        self.__fill_water_heater_repository.switch_heater_on()
        water_temperature = 0
        while water_temperature < 25:
            water_temperature = self.__water_temperature_controller.read_device_temperature()
            print("Water temperature: " + str(self.__water_temperature_controller.read_device_temperature()))
            time.sleep(10)
        self.__fill_water_heater_repository.switch_heater_off()
