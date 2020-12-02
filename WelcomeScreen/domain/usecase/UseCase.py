import time

from dependency_injector.wiring import Provide, inject
from WelcomeScreen.WelcomeScreenContainer import Container
from WelcomeScreen.data.controller.LCDController import WelcomeScreenController
from WelcomeScreen.data.repository import VersionRepository
from WelcomeScreen.domain.exception.NoVersionException import NoVersionException


class WelcomeScreenUseCase:

    @inject
    def __init__(self, controller: WelcomeScreenController = Provide[Container.welcomeController]):
        self.__controller = controller

    def show_screen(self):
        self.__controller.build_frame()
        self.__controller.write_user_message("Pablo")
        try:
            self.__controller.write_version_message(str(VersionRepository.get_version_code(), "utf-8"))
            time.sleep(5)
        except NoVersionException:
            pass

        self.__controller.write_initialising_message()
