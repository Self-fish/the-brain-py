from HandleLights.data.controller.Controller import LightsController
from HandleLights.domain.model.LightStatus import LightStatus


class LightStatusRepository:

    def __init__(self):
        self.__light_controller = LightsController()
        self.__current_light_status = LightStatus.OFF

    def update_light_status(self, light_status):
        if light_status != self.__current_light_status:
            self.__light_controller.update_light_status(light_status)
            self.__current_light_status = light_status
