from dependency_injector.wiring import Provide, inject

from Core.data.device import LCDStatus
from Core.data.driver.RelayStatus import RelayStatus
from CoreMenu.domain.usecase.MenuUseCase import MenuUseCase
from HandleLightMenu.domain.model.LightMenuOptions import LightMenuOptions
from HandleLights.HandleLightsContainer import HandleLightsContainer
from HandleLights.data.repository.LightStatus import LightStatusRepository
from MainScreen.MainScreenContainer import MainScreenContainer
from MainScreen.data.controller.LCDController import MainScreenController


@MenuUseCase.register
class DisplayLightMenuUseCase(MenuUseCase):

    @inject
    def __init__(self, screen_controller: MainScreenController = Provide[MainScreenContainer.main_screen_controller],
                 light_repository: LightStatusRepository = Provide[HandleLightsContainer.light_status_repository]):
        super().__init__(screen_controller)
        self.__screen_repository = screen_controller
        self.__light_repository = light_repository

    def build_menu_options(self):
        self.menu_options = [LightMenuOptions.AUTOMATIC]
        self.menu_options.append(self.__light_status_to_display())

    def select_option(self):
        LCDStatus.lcd_next_status = LCDStatus.LCDStatus.MAIN_SCREEN

    def __light_status_to_display(self):
        if self.__light_repository.current_light_status == RelayStatus.ON:
            return LightMenuOptions.MANUAL_OFF
        else:
            return LightMenuOptions.MANUAL_ON
