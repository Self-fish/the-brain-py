from dependency_injector import containers, providers

from Core.data.driver.RelayController import RelayController
from EmptyAquariumAction.data.repository.FilterRepository import FilterRepository


class EmptyAquariumActionContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    filter_controller = providers.Factory(RelayController, 1)
    filter_repository = providers.Singleton(FilterRepository, filter_controller)
