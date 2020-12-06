import sys
import threading
import time

from HandleLights.domain.usecase.UseCase import HandleLightsUseCase
from MainScreen.domain.usecase.UseCase import MainScreenUseCase
from WelcomeScreen.WelcomeScreenContainer import WelcomeContainer
from HandleLights.HandleLightsContainer import HandleLightsContainer
from WelcomeScreen.domain.usecase.UseCase import WelcomeScreenUseCase


def handle_lights(lights_use_case: HandleLightsUseCase):
    while True:
        lights_use_case.handle_lights()
        time.sleep(60)


def handle_main_screen(main_screen_use_case: MainScreenUseCase):
    while True:
        main_screen_use_case.show_next_value()
        time.sleep(5)


if __name__ == '__main__':
    welcome_container = WelcomeContainer()
    welcome_container.wire(modules=[sys.modules[__name__]])
    handle_lights_container = HandleLightsContainer()
    handle_lights_container.wire(modules=[sys.modules[__name__]])

    welcome_screen_use_case = WelcomeScreenUseCase()
    welcome_screen_use_case.show_screen()

    handle_light_use_case = HandleLightsUseCase()
    handle_lights_thread = threading.Thread(target=handle_lights, args=(handle_light_use_case,))
    handle_lights_thread.start()
    
    main_screen_use_case = MainScreenUseCase()
    handle_main_screen_thread = threading.Thread(target=handle_main_screen, args=(main_screen_use_case,))
    handle_main_screen_thread.start()

