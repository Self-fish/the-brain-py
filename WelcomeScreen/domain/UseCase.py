from dependency_injector.wiring import Provide, inject
from WelcomeScreen.WelcomeScreenContainer import Container
from WelcomeScreen.data.LCDController import WelcomeScreenController


class WelcomeScreenUseCase:

    @inject
    def __init__(self, controller: WelcomeScreenController = Provide[Container.welcomeController]):
        self.__controller = controller

    def show_screen(self):
        self.__controller.show_welcome_message()
