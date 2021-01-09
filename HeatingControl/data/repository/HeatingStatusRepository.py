from Core.data.driver.RelayController import RelayController
from Core.data.driver.RelayStatus import RelayStatus
from HeatingControl.domain.model.HeatingActive import HeatingActive


class HeatingStatusRepository:

    max_retries = 10

    def __init__(self, first_heating_controller: RelayController, second_heating_controller: RelayController):
        self.__first_heating_controller = first_heating_controller
        self.__second_heating_controller = second_heating_controller
        self.__current_heating_status = RelayStatus.OFF
        self.heating_active: HeatingActive = HeatingActive.NONE
        self.__number_of_tries = 0
        self.__previous_temperature = 0

    def update_heating_status(self, heating_status, current_temperature):
        if heating_status == RelayStatus.ON and current_temperature is not 0:
            print("Previous Temperature: " + str(self.__previous_temperature))
            print("Current Temperature: " + str(current_temperature))
            print("Queremos activar")
            if self.__current_heating_status == RelayStatus.OFF:
                print("Venimos de apagado. Encendemos el primer calentador")
                print("")
                self.__activate_heating(current_temperature)

            elif self.__previous_temperature == current_temperature:
                print("Venimos de encendido pero la temperatura es igual")
                if self.__number_of_tries < self.max_retries:
                    print("Probamos otra vez")
                    print("")
                    self.__number_of_tries += 1
                else:
                    print("Necesitamos mas potencia")
                    print("")
                    self.__activate_heating(current_temperature)

            elif self.__previous_temperature > current_temperature:
                print("Necesitamos mas potencia")
                print("")
                self.__activate_heating(current_temperature)

            elif self.__previous_temperature < current_temperature:
                print("Vamos mejorando")
                print("")
                self.__previous_temperature = current_temperature

        else:
            print("Queremos desactivar")
            print("")
            self.__deactivate_heating()

    def __first_heating_on(self):
        print("Activamos el heating 1")
        self.__first_heating_controller.update_relay_status(RelayStatus.ON)

    def __second_heating_on(self):
        print("Activamos el heating 2")
        #self.__second_heating_controller.update_relay_status(RelayStatus.ON)
        #self.__first_heating_controller.update_relay_status(RelayStatus.OFF)

    def __both_heating_on(self):
        print("Activamos los dos heatings")
        #self.__second_heating_controller.update_relay_status(RelayStatus.ON)
        self.__first_heating_controller.update_relay_status(RelayStatus.ON)

    def __activate_heating(self, current_temperature):
        if self.heating_active == HeatingActive.NONE:
            self.__first_heating_on()
            self.heating_active = HeatingActive.FIRST_HEATING
        elif self.heating_active == HeatingActive.FIRST_HEATING:
            self.__second_heating_on()
            self.heating_active = HeatingActive.SECOND_HEATING
        elif self.heating_active == HeatingActive.SECOND_HEATING:
            self.__both_heating_on()
            self.heating_active = HeatingActive.BOTH
        else:
            self.__both_heating_on()
            self.heating_active = HeatingActive.BOTH
        self.__previous_temperature = current_temperature
        self.__number_of_tries = 0
        self.__current_heating_status = RelayStatus.ON

    def __deactivate_heating(self):
        self.__second_heating_controller.update_relay_status(RelayStatus.OFF)
        self.__first_heating_controller.update_relay_status(RelayStatus.OFF)
        self.__current_heating_status = RelayStatus.OFF
        self.heating_active = HeatingActive.NONE

