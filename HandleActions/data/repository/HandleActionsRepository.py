from HandleActions.data.datasource.CustomKafkaConsumer import CustomKafkaConsumer


class HandleActionsRepository:

    def __init__(self, consumer: CustomKafkaConsumer):
        self.__consumer = consumer
        self.__consumer.add_listener(self.__process_action)

    def __process_action(self, message):
        print(message)

    def listen_actions(self):
        self.__consumer.read()
