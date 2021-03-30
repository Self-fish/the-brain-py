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
from HeaterControl.domain.usecase import UseCase


class FillAquariumUseCase(CoreActionUseCase):

    DESIRED_NEW_WATER_TEMPERATURE = 25
    CONTAINER_MAX_CAPACITY = 4
    AQUARIUM_MAX_CAPACITY = 6

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
        self.__prepare_aquarium()
        #self.__heat_water()
        current_distance = self.__empty_aquarium()
        print("Final distance: " + str(current_distance))
        if self.__is_aquarium_totally_filled(current_distance):
            self.__finish_fill_action()

    def __prepare_aquarium(self):
        self.__fill_pump_repository.switch_pump_off()

    def __heat_water(self):
        self.__fill_water_heater_repository.switch_heater_on()
        water_temperature = 0
        while water_temperature < self.DESIRED_NEW_WATER_TEMPERATURE:
            water_temperature = self.__water_temperature_controller.read_device_temperature()
            time.sleep(5)
        self.__fill_water_heater_repository.switch_heater_off()

    def __empty_aquarium(self):
        original_distance = MCP3008Controller.calculate_distance()
        print("Original distance: " + str(original_distance))
        current_distance = 99
        self.__fill_pump_repository.switch_pump_on()
        while current_distance > original_distance - self.CONTAINER_MAX_CAPACITY:
            current_distance = MCP3008Controller.calculate_distance()
            print("Distance now: " + str(current_distance))
            if self.__is_aquarium_totally_filled(current_distance):
                print("Aquarium totally filled")
                break
        self.__fill_pump_repository.switch_pump_off()
        return current_distance

    def __is_aquarium_totally_filled(self, current_distance):
        if current_distance < self.AQUARIUM_MAX_CAPACITY:
            return True
        else:
            return False

    def __finish_fill_action(self):
        print("Finish fill action")
        self.__filter_repository.switch_filter_on()
        self.__general_heater_use_case.unblock_heaters()
