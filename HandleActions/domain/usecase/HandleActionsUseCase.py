from dependency_injector.wiring import inject, Provide

from Core.domain.usecases.CoreActionUseCase import CoreActionUseCase
from HandleActions.HandleActionsContainer import HandleActionsContainer
from HandleActions.data.repository.HandleActionsRepository import HandleActionsRepository
from HandleActions.domain.usecase import ActionsUseCaseFactory


class HandleActionsUseCase:

    @inject
    def __init__(self, repository: HandleActionsRepository = Provide[HandleActionsContainer.handle_actions_repository]):
        self.__repository = repository
        self.__repository.add_listener(self.__process_action)
        self.__use_case: CoreActionUseCase = None

    def read_messages(self):
        self.__repository.listen_actions()

    def __process_action(self, action):
        self.__use_case = ActionsUseCaseFactory.build_use_case(action)
        self.__use_case.execute_action(action)

