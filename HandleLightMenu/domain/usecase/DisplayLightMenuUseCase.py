from dependency_injector.wiring import Provide, inject

from Core.data.device import LCDStatus
from Core.data.driver.RelayStatus import RelayStatus
from CoreMenu.domain.usecase.MenuUseCase import MenuUseCase
from HandleLightMenu.data.repository import HandleLightMenuRepository
from HandleLightMenu.domain.model.LightMenuOptions import LightMenuOptions
from HandleLights.HandleLightsContainer import HandleLightsContainer
from HandleLights.data.repository.LightStatus import LightStatusRepository
from HandleLights.domain.usecase.UseCase import HandleLightsUseCase
from MainScreen.MainScreenContainer import MainScreenContainer
from MainScreen.data.controller.LCDController import MainScreenController


@MenuUseCase.register
class DisplayLightMenuUseCase(MenuUseCase):

    @inject
    def __init__(self, screen_controller: MainScreenController = Provide[MainScreenContainer.main_screen_controller],
                 light_repository: LightStatusRepository = Provide[HandleLightsContainer.light_status_repository]):
        super().__init__(screen_controller)
        self.__light_repository = light_repository
        self.__handle_lights_use_case: HandleLightsUseCase = None

    def lazy_injection(self, handle_light_use_case: HandleLightsUseCase):
        self.__handle_lights_use_case = handle_light_use_case

    def build_menu_options(self):
        self.menu_options = [LightMenuOptions.AUTOMATIC]
        self.menu_options.append(self.__light_status_to_display())

    def select_option(self):
        update_result = HandleLightMenuRepository.update_light_preferences(self.menu_options[self.selected_option])
        if not update_result:
            self.display_error_message("Ups, error!")
        else:
            self.__handle_lights_use_case.handle_lights()
        LCDStatus.lcd_next_status = LCDStatus.LCDStatus.MAIN_SCREEN

    def __light_status_to_display(self):
        if self.__light_repository.current_light_status == RelayStatus.ON:
            return LightMenuOptions.MANUAL_OFF
        else:
            return LightMenuOptions.MANUAL_ON
