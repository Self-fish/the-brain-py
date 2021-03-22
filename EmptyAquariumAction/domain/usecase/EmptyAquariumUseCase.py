from dependency_injector.wiring import inject, Provide

from Core.data.driver.RelayStatus import RelayStatus
from Core.domain.usecases.CoreActionUseCase import CoreActionUseCase
from EmptyAquariumAction.EmptyAquariumActionContainer import EmptyAquariumActionContainer
from EmptyAquariumAction.data.controller import MCP3008Controller
from EmptyAquariumAction.data.repository.EmptyPumpRepository import EmptyPumpRepository
from EmptyAquariumAction.data.repository.FillWaterHeaterRepository import FillWaterHeaterRepository
from EmptyAquariumAction.data.repository.FilterRepository import FilterRepository
from HeaterControl.HeaterControlContainer import HeaterControlContainer
from HeaterControl.data.repository.HeaterStatusRepository import HeaterStatusRepository


class EmptyAquariumUseCase(CoreActionUseCase):

    @inject
    def __init__(self, filter_repository: FilterRepository = Provide[EmptyAquariumActionContainer.filter_repository],
                 empty_pump_repository: EmptyPumpRepository =
                 Provide[EmptyAquariumActionContainer.empty_pump_repository],
                 fill_water_heater_repository: FillWaterHeaterRepository =
                 Provide[EmptyAquariumActionContainer.fill_water_heater_repository],
                 general_heater_repository: HeaterStatusRepository =
                 Provide[HeaterControlContainer.heater_status_repository]):
        self.__filter_repository = filter_repository
        self.__empty_pump_repository = empty_pump_repository
        self.__fill_water_heater_repository = fill_water_heater_repository
        self.__general_heater_repository = general_heater_repository

    def execute_action(self):
        # 1. Encender el calendator del cubo de llenado
        # 2. Parar el Filtro
        # 3. Empezar a vaciar hasta el valor que toque
        # 4. Parar el calentador del cubo de llenado
        self.__general_heater_repository.turn_off_heater_and_block()
        self.__fill_water_heater_repository.switch_heater_on()
        self.__filter_repository.switch_filter_off()
        original_distance = MCP3008Controller.calculate_distance()
        print("Original distance: " + str(original_distance))
        print(original_distance + 4.5)
        distance = 0
        self.__empty_pump_repository.switch_pump_on()

        while distance < original_distance + 4.5:
            distance = MCP3008Controller.calculate_distance()
            print(distance)

        self.__empty_pump_repository.switch_pump_off()
        self.__fill_water_heater_repository.switch_heater_off()

