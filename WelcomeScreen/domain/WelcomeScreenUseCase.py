from dependency_injector.wiring import Provide, inject
from WelcomeScreen.Containers import Container
from WelcomeScreen.data.WelcomeScreenController import WelcomeScreenController


class WelcomeScreenUseCase:

    @inject
    def __init__(self, controller: WelcomeScreenController = Provide[Container.welcomeController]):
        self.controller = controller

    def show_screen(self):
        self.controller.show_welcome_message()
