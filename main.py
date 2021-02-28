import sys
import threading
import time

from Core.data.repository import Notifications
from HandleLights.domain.usecase.UseCase import HandleLightsUseCase
from HeaterControl.HeaterControlContainer import HeaterControlContainer
from HeaterControl.domain.usecase.UseCase import HeaterControlUseCase
from MainScreen.MainScreenContainer import MainScreenContainer
from MainScreen.domain.usecase.UseCase import MainScreenUseCase
from MeasureWaterTemp.MeasureWaterTempContainer import MeasureWaterTempContainer
from MeasureWaterTemp.domain.usecase.UseCase import MeasureWaterTempUseCase
from WelcomeScreen.WelcomeScreenContainer import WelcomeContainer
from HandleLights.HandleLightsContainer import HandleLightsContainer
from WelcomeScreen.domain.usecase.UseCase import WelcomeScreenUseCase


def handle_lights(use_case: HandleLightsUseCase):
    while True:
        use_case.handle_lights()
        time.sleep(60)


def handle_main_screen(use_case: MainScreenUseCase):
    while True:
        use_case.show_next_value()
        time.sleep(5)


def measure_water_temp(use_case: MeasureWaterTempUseCase):
    while True:
        use_case.track_water_temp()
        time.sleep(60)


def control_heating(use_case: HeaterControlUseCase):
    while True:
        use_case.control_heating()
        time.sleep(60)


if __name__ == '__main__':
    welcome_container = WelcomeContainer()
    welcome_container.wire(modules=[sys.modules[__name__]])
    handle_lights_container = HandleLightsContainer()
    handle_lights_container.wire(modules=[sys.modules[__name__]])
    main_screen_container = MainScreenContainer()
    main_screen_container.wire(modules=[sys.modules[__name__]])
    heating_control_container = HeaterControlContainer()
    heating_control_container.wire(modules=[sys.modules[__name__]])
    measure_water_container = MeasureWaterTempContainer()
    measure_water_container.wire(modules=[sys.modules[__name__]])

    welcome_screen_use_case = WelcomeScreenUseCase()
    welcome_screen_use_case.show_screen()

    handle_light_use_case = HandleLightsUseCase()
    handle_lights_thread = threading.Thread(target=handle_lights, args=(handle_light_use_case,))
    handle_lights_thread.start()

    measure_water_temp_use_case = MeasureWaterTempUseCase()
    measure_water_temp_thread = threading.Thread(target=measure_water_temp, args=(measure_water_temp_use_case,))
    measure_water_temp_thread.start()

    main_screen_use_case = MainScreenUseCase()
    handle_main_screen_thread = threading.Thread(target=handle_main_screen, args=(main_screen_use_case,))
    handle_main_screen_thread.start()

    heating_control_use_case = HeaterControlUseCase()
    handle_heating_control_thread = threading.Thread(target=control_heating, args=(heating_control_use_case,))
    handle_heating_control_thread.start()





