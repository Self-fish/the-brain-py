from dependency_injector import containers, providers

from HandleActions.data.datasource.CustomKafkaConsumer import CustomKafkaConsumer
from HandleActions.data.repository.HandleActionsRepository import HandleActionsRepository


class HandleActionsContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    kafka_consumer = providers.Factory(CustomKafkaConsumer)
    handle_actions_repository = providers.Factory(HandleActionsRepository, kafka_consumer)
