from HandleActions.data.datasource.CustomKafkaConsumer import CustomKafkaConsumer
from HandleActions.data.repository.HandleActionsRepository import HandleActionsRepository


class HandleActionsUseCase:

    def __init__(self):
        self.__repository = HandleActionsRepository(CustomKafkaConsumer())

    def read_messages(self):
        print("We are about to read message from the kafka queue")
        self.__repository.listen_actions()
