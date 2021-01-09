from dependency_injector.wiring import Provide, inject

from CoreMenu.domain.usecase.MenuUseCase import MenuUseCase
from HandleAlerts.HandleAlertsContainer import HandleAlertsContainer
from HandleAlerts.data.repository.AlertsRepository import AlertsRepository
from HandleAlerts.domain.usecase.ShowAlerts import ShowAlerts
from HandleGeneralMenu.domain.model.GeneralMenuOptions import GeneralMenuOptions
from HandleLightMenu.domain.usecase.DisplayLightMenuUseCase import DisplayLightMenuUseCase
from MainScreen.MainScreenContainer import MainScreenContainer
from MainScreen.data.controller.LCDController import MainScreenController


@MenuUseCase.register
class DisplayGeneralMenuUseCase(MenuUseCase):

    @inject
    def __init__(self, alerts_repository: AlertsRepository = Provide[HandleAlertsContainer.alerts_repository],
                 screen_controller: MainScreenController = Provide[MainScreenContainer.main_screen_controller]):
        super().__init__(screen_controller)
        self.__alerts_repository = alerts_repository
        self.__show_alerts_use_case: ShowAlerts = None
        self.__display_light_menu_use_case: DisplayLightMenuUseCase = None

    def lazy_injection(self, show_alerts_use_case: ShowAlerts, display_light_menu_use_case: DisplayLightMenuUseCase):
        self.__show_alerts_use_case = show_alerts_use_case
        self.__display_light_menu_use_case = display_light_menu_use_case

    def build_menu_options(self):
        if len(self.__alerts_repository.get_alerts()) == 0:
            self.menu_options = [GeneralMenuOptions.LIGHT_CONTROL]
        else:
            self.menu_options = [GeneralMenuOptions.SHOW_ALERTS, GeneralMenuOptions.LIGHT_CONTROL]

    def select_option(self):
        if self.menu_options[self.selected_option] == GeneralMenuOptions.SHOW_ALERTS:
            self.__show_alerts_use_case.display_alerts(0)
        else:
            self.__display_light_menu_use_case.display_menu()