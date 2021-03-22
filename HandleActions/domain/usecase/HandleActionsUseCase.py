from dependency_injector.wiring import inject, Provide

from Core.domain.usecases.CoreActionUseCase import CoreActionUseCase
from HandleActions.HandleActionsContainer import HandleActionsContainer
from HandleActions.data.repository.HandleActionsRepository import HandleActionsRepository
from HandleActions.domain.usecase import ActionsUseCaseFactory
from HeaterControl.domain.usecase import UseCase


class HandleActionsUseCase:

    @inject
    def __init__(self, repository: HandleActionsRepository = Provide[HandleActionsContainer.handle_actions_repository]):
        self.__repository = repository
        self.__repository.add_listener(self.__process_action)
        self.__general_heater_use_case = None
        self.__use_case: CoreActionUseCase = None

    def lazy_injection(self, general_heater_use_case: UseCase):
        self.__general_heater_use_case = general_heater_use_case

    def read_messages(self):
        self.__repository.listen_actions()

    def __process_action(self, action):
        self.__use_case = ActionsUseCaseFactory.build_use_case(action)
        self.__use_case.execute_action()

