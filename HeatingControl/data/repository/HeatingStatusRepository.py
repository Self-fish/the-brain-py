from Core.data.driver.RelayController import RelayController
from Core.data.driver.RelayStatus import RelayStatus
from HeatingControl.domain.model.HeatingActive import HeatingActive


class HeatingStatusRepository:

    max_retries = 5

    def __init__(self, first_heating_controller: RelayController, second_heating_controller: RelayController):
        self.__first_heating_controller = first_heating_controller
        self.__second_heating_controller = second_heating_controller
        self.heating_active: HeatingActive = HeatingActive.NONE
        self.__number_of_tries = 0
        self.__previous_temperature = 0
        self.__turn_off_heating()

    def __turn_off_heating(self):
        self.__manage_first_heating(RelayStatus.OFF)
        self.__manage_second_heating(RelayStatus.OFF)

    def update_heating_status(self, heating_status, current_temperature):
        if heating_status == RelayStatus.ON and current_temperature is not 0:
            print("Previous Temperature: " + str(self.__previous_temperature))
            print("Current Temperature: " + str(current_temperature))
            print("Queremos activar")
            if self.heating_active == HeatingActive.NONE:
                print("Venimos de apagado.")
                self.__activate_heating(current_temperature)

            elif self.__previous_temperature == current_temperature:
                print("Venimos de encendido pero la temperatura es igual")
                if self.__number_of_tries < self.max_retries:
                    print("Probamos otra vez")
                    print("")
                    self.__number_of_tries += 1
                else:
                    print("Necesitamos mas potencia")
                    self.__activate_heating(current_temperature)

            elif self.__previous_temperature > current_temperature:
                print("Necesitamos mas potencia")
                self.__activate_heating(current_temperature)

            elif self.__previous_temperature < current_temperature:
                print("Vamos mejorando")
                print("")
                self.__previous_temperature = current_temperature

        else:
            print("Queremos desactivar")
            print("")
            self.__previous_temperature = current_temperature
            self.__deactivate_heating()

    def __manage_first_heating(self, relay_status):
        print("Heating 1: " + str(relay_status))
        self.__first_heating_controller.update_relay_status(relay_status)

    def __manage_second_heating(self, relay_status):
        print("Heating2: " + str(relay_status))
        self.__second_heating_controller.update_relay_status(relay_status)

    def __activate_heating(self, current_temperature):
        if self.heating_active == HeatingActive.NONE:
            print("Activamos el primer heating")
            self.__manage_first_heating(RelayStatus.ON)
            self.heating_active = HeatingActive.FIRST_HEATING
            print("")
        elif self.heating_active == HeatingActive.FIRST_HEATING:
            print("Activamos el segundo heating")
            self.__manage_first_heating(RelayStatus.OFF)
            self.__manage_second_heating(RelayStatus.ON)
            self.heating_active = HeatingActive.SECOND_HEATING
            print("")
        elif self.heating_active == HeatingActive.SECOND_HEATING:
            print("Activamos los dos")
            self.__manage_first_heating(RelayStatus.ON)
            self.__manage_second_heating(RelayStatus.ON)
            self.heating_active = HeatingActive.BOTH
            print("")
        self.__previous_temperature = current_temperature
        self.__number_of_tries = 0

    def __deactivate_heating(self):
        if self.heating_active == HeatingActive.FIRST_HEATING:
            print("Apagamos todo")
            self.__manage_first_heating(RelayStatus.OFF)
            self.__manage_second_heating(RelayStatus.OFF)
            self.heating_active = HeatingActive.NONE
            print("")
        elif self.heating_active == HeatingActive.SECOND_HEATING:
            print("Dejamos solo el 1")
            self.__manage_first_heating(RelayStatus.ON)
            self.__manage_second_heating(RelayStatus.OFF)
            self.heating_active = HeatingActive.FIRST_HEATING
            print("")
        elif self.heating_active == HeatingActive.BOTH:
            print("Dejamos solo el 2")
            self.__manage_first_heating(RelayStatus.OFF)
            self.__manage_second_heating(RelayStatus.ON)
            self.heating_active = HeatingActive.SECOND_HEATING
            print("")
        self.__number_of_tries = 0


