from dependency_injector.wiring import Provide, inject
from WelcomeScreen.WelcomeScreenContainer import Container
from WelcomeScreen.data.LCDController import WelcomeScreenController


class WelcomeScreenUseCase:

    @inject
    def __init__(self, controller: WelcomeScreenController = Provide[Container.welcomeController]):
        self.__controller = controller

    def show_screen(self):
        self.__controller.build_frame()
        self.__controller.write_user_message("Pablo")
        self.__controller.write_version_message("0.1")
        self.__controller.write_initialising_message()
