from HandleActions.data.datasource.CustomKafkaConsumer import CustomKafkaConsumer
from HandleActions.data.repository.HandleActionsRepository import HandleActionsRepository


class HandleActionsUseCase:

    def __init__(self):
        self.__repository = HandleActionsRepository(CustomKafkaConsumer())
        self.__repository.add_listener(self.__process_action)

    def read_messages(self):
        print("We are about to read message from the kafka queue")
        self.__repository.listen_actions()

    def __process_action(self, action):
        print("Action received")
        print(action.action)
        print(action.step)

