from Core.data.driver.Controller import RelayController


class LightStatusRepository:

    def __init__(self, light_controller: RelayController):
        self.__light_controller = light_controller
        self.__current_light_status = self.__light_controller.get_current_relay_status()

    def update_light_status(self, light_status):

        if light_status != self.__current_light_status:
            self.__light_controller.update_relay_status(light_status)
            self.__current_light_status = light_status
