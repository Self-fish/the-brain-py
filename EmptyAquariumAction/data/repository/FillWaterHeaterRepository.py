from Core.data.driver.RelayController import RelayController
from Core.data.driver.RelayStatus import RelayStatus


class FillWaterHeaterRepository:

    def __init__(self, fill_water_heater_controller: RelayController):
        self.__fill_water_heater_controller = fill_water_heater_controller
        self.__water_heater_status = RelayStatus.OFF

    def switch_heater_off(self):
        if self.__water_heater_status != RelayStatus.OFF:
            print("Apagamos el calentador del agua de llenado")
            self.__fill_water_heater_controller.update_relay_status(RelayStatus.OFF)
            self.__water_heater_status = RelayStatus.OFF

    def switch_heater_on(self):
        if self.__water_heater_status != RelayStatus.OFF:
            print("Encendemos el calentador del agua de llenado")
            self.__fill_water_heater_controller.update_relay_status(RelayStatus.ON)
            self.__water_heater_status = RelayStatus.ON
