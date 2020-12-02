import time
from subprocess import CalledProcessError

from dependency_injector.wiring import Provide, inject
from WelcomeScreen.WelcomeScreenContainer import Container
from WelcomeScreen.data.controller.LCDController import WelcomeScreenController
from WelcomeScreen.data.repository import VersionRepository


class WelcomeScreenUseCase:

    @inject
    def __init__(self, controller: WelcomeScreenController = Provide[Container.welcomeController]):
        self.__controller = controller

    def show_screen(self):
        self.__controller.build_frame()
        self.__controller.write_user_message("Pablo")
        self.__controller.write_version_message(VersionRepository.get_version_code())
        time.sleep(5)
        self.__controller.write_initialising_message()
