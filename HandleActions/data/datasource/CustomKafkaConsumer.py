from kafka import KafkaConsumer


class CustomKafkaConsumer:

    __bootstrap_servers = ['192.168.0.15:9092']
    __topic_name = 'aquarium_actions'

    def __init__(self):
        self.__on_message_receive = []

    def add_listener(self, listener):
        self.__on_message_receive.append(listener)

    def read(self):
        consumer = KafkaConsumer(self.__topic_name, auto_offset_reset='latest',
                                 bootstrap_servers=self.__bootstrap_servers, api_version=(0, 10))
        for msg in consumer:
            self.__fire_event(msg.value)

    def __fire_event(self, message):
        for listener in self.__on_message_receive:
            listener(message)
