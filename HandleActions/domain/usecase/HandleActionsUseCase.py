from dependency_injector.wiring import inject, Provide

from HandleActions.HandleActionsContainer import HandleActionsContainer
from HandleActions.data.repository.HandleActionsRepository import HandleActionsRepository


class HandleActionsUseCase:

    @inject
    def __init__(self, repository: HandleActionsRepository = Provide[HandleActionsContainer.handle_actions_repository]):
        self.__repository = repository
        self.__repository.add_listener(self.__process_action)

    def read_messages(self):
        self.__repository.listen_actions()

    def __process_action(self, action):
        print(action.action)
        print(action.step)

