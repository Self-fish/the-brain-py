from dependency_injector.wiring import Provide, inject

from Core.data.driver.RelayStatus import RelayStatus
from HandleLightMenu.domain.model.LightMenuOptions import LightMenuOptions
from HandleLights.HandleLightsContainer import HandleLightsContainer
from HandleLights.data.repository.LightStatus import LightStatusRepository
from MainScreen.MainScreenContainer import MainScreenContainer
from MainScreen.data.controller.LCDController import MainScreenController


class DisplayLightMenuUseCase:

    @inject
    def __init__(self, screen_controller: MainScreenController = Provide[MainScreenContainer.main_screen_controller],
                 light_repository: LightStatusRepository = Provide[HandleLightsContainer.light_status_repository]):
        self.__screen_repository = screen_controller
        self.__menu_options = [LightMenuOptions.AUTOMATIC, LightMenuOptions.MANUAL_OFF]
        self.__light_repository = light_repository
        self.__selected_option = 0

    def display_light_menu(self):
        self.__build_menu()
        self.__screen_repository.print_menu(self.__menu_options, self.__menu_options[self.__selected_option])

    def __build_menu(self):
        self.__menu_options.remove(LightMenuOptions.MANUAL_OFF)
        self.__menu_options.remove(LightMenuOptions.MANUAL_ON)
        self.__menu_options.append(self.__light_status_to_display())

    def __light_status_to_display(self):
        if self.__light_repository.current_light_status == RelayStatus.ON:
            return LightMenuOptions.MANUAL.OFF
        else:
            return LightMenuOptions.MANUAL.ON
