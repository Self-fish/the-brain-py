from dependency_injector.wiring import inject, Provide

from Core.domain.usecases.CoreActionUseCase import CoreActionUseCase
from EmptyAquariumAction.EmptyAquariumActionContainer import EmptyAquariumActionContainer
from EmptyAquariumAction.data.controller import MCP3008Controller
from EmptyAquariumAction.data.repository.EmptyPumpRepository import EmptyPumpRepository
from EmptyAquariumAction.data.repository.FillWaterHeaterRepository import FillWaterHeaterRepository
from EmptyAquariumAction.data.repository.FilterRepository import FilterRepository
from HandleLights.domain.usecase.UseCase import HandleLightsUseCase
from HeaterControl.domain.usecase import UseCase



class EmptyAquariumUseCase(CoreActionUseCase):

    CONTAINER_MAX_CAPACITY = 4.5

    @inject
    def __init__(self, filter_repository: FilterRepository = Provide[EmptyAquariumActionContainer.filter_repository],
                 empty_pump_repository: EmptyPumpRepository =
                 Provide[EmptyAquariumActionContainer.empty_pump_repository],
                 fill_water_heater_repository: FillWaterHeaterRepository =
                 Provide[EmptyAquariumActionContainer.fill_water_heater_repository]):
        self.__filter_repository = filter_repository
        self.__empty_pump_repository = empty_pump_repository
        self.__fill_water_heater_repository = fill_water_heater_repository
        self.__general_heater_use_case: UseCase = None
        self.__light_use_case: HandleLightsUseCase = None

    def lazy_injection(self, general_heater_use_case: UseCase, light_use_case: HandleLightsUseCase):
        self.__general_heater_use_case = general_heater_use_case
        self.__light_use_case = light_use_case

    def execute_action(self):
        self.__prepare_aquarium()
        self.__empty_aquarium()
        #self.__fill_water_heater_repository.switch_heater_off()

    def __prepare_aquarium(self):
        self.__general_heater_use_case.switch_off_heater_and_block()
        # self.__fill_water_heater_repository.switch_heater_on()
        self.__filter_repository.switch_filter_off()
        self.__light_use_case.turn_on_light()

    def __empty_aquarium(self):
        original_distance = MCP3008Controller.calculate_distance()
        print("Original distance: " + str(original_distance))
        print("Max capacity: " + str(self.CONTAINER_MAX_CAPACITY))
        distance = 0
        self.__empty_pump_repository.switch_pump_on()
        while distance < (original_distance + self.CONTAINER_MAX_CAPACITY):
            distance = MCP3008Controller.calculate_distance()
            print(distance)
        self.__empty_pump_repository.switch_pump_off()
