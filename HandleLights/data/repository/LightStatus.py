from HandleLights.data.controller.Controller import LightsController


class LightStatusRepository:

    def __init__(self, light_controller: LightsController):
        self.__light_controller = light_controller
        self.__current_light_status = self.__light_controller.get_current_light_status()

    def update_light_status(self, light_status):

        if light_status != self.__current_light_status:
            self.__light_controller.update_light_status(light_status)
            self.__current_light_status = light_status
