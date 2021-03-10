from HandleActions.data.datasource.CustomKafkaConsumer import CustomKafkaConsumer
from HandleActions.domain.model.Action import Action
import json


class HandleActionsRepository:

    def __init__(self, consumer: CustomKafkaConsumer):
        self.__consumer = consumer
        self.__consumer.add_listener(self.__process_action)
        self.__listeners = []

    def __process_action(self, message):
        string_message = message.decode("utf-8")
        #action_json = json.load(message.decode("utf-8"))
        print(string_message)
        #action = Action(action_json.json()['action'], message.decode("utf-8").json()['step'])
        #self.__fire_event(action)

    def add_listener(self, listener):
        self.__listeners.append(listener)

    def __fire_event(self, action: Action):
        for listener in self.__listeners:
            listener(action)

    def listen_actions(self):
        self.__consumer.read()
