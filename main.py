import sys
import threading
import time

from Core.data.driver import JoystickController
from HandleAlerts.HandleAlertsContainer import HandleAlertsContainer
from HandleAlerts.domain.usecase.GetAlertsUseCase import GetAlertsUseCase
from HandleAlerts.domain.usecase.ShowAlerts import ShowAlerts
from HandleAlerts.domain.usecase.ShowAlertsAdviseUseCase import ShowAlertsAdviseUseCase
from HandleLightMenu.domain.usecase.DisplayLightMenuUseCase import DisplayLightMenuUseCase
from HandleLights.domain.usecase.UseCase import HandleLightsUseCase
from HandleGeneralMenu.domain.usecase.DisplayGeneralMenuUseCase import DisplayGeneralMenuUseCase
from HeatingControl.HeatingControlContainer import HeatingControlContainer
from HeatingControl.domain.usecase.UseCase import HeatingControlUseCase
from MainScreen.MainScreenContainer import MainScreenContainer
from MainScreen.domain.usecase.UseCase import MainScreenUseCase
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


def control_heating(use_case: HeatingControlUseCase):
    while True:
        use_case.control_heating()
        time.sleep(60)


def get_alerts(use_case: GetAlertsUseCase):
    while True:
        use_case.get_alerts()
        time.sleep(60)


def show_alert_advice(use_case: ShowAlertsAdviseUseCase):
    while True:
        use_case.show_alert_advice()
        time.sleep(60)


def display_menu(use_case: DisplayGeneralMenuUseCase):
    while True:
        if JoystickController.is_switch_pressed():
            use_case.display_menu()
        time.sleep(1)


if __name__ == '__main__':
    welcome_container = WelcomeContainer()
    welcome_container.wire(modules=[sys.modules[__name__]])
    handle_lights_container = HandleLightsContainer()
    handle_lights_container.wire(modules=[sys.modules[__name__]])
    main_screen_container = MainScreenContainer()
    main_screen_container.wire(modules=[sys.modules[__name__]])
    heating_control_container = HeatingControlContainer()
    heating_control_container.wire(modules=[sys.modules[__name__]])
    handle_alerts_container = HandleAlertsContainer()
    handle_alerts_container.wire(modules=[sys.modules[__name__]])

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

    heating_control_use_case = HeatingControlUseCase()
    handle_heating_control_thread = threading.Thread(target=control_heating, args=(heating_control_use_case,))
    handle_heating_control_thread.start()

    get_alerts_use_case = GetAlertsUseCase()
    get_alerts_thread = threading.Thread(target=get_alerts, args=(get_alerts_use_case,))
    get_alerts_thread.start()

    show_alert_advice_use_case = ShowAlertsAdviseUseCase()
    show_alerts_advice_thread = threading.Thread(target=show_alert_advice, args=(show_alert_advice_use_case,))
    show_alerts_advice_thread.start()

    display_light_menu_use_case = DisplayLightMenuUseCase()
    display_light_menu_use_case.lazy_injection(HandleLightsUseCase())
    display_menu_use_case = DisplayGeneralMenuUseCase()
    display_menu_use_case.lazy_injection(ShowAlerts(), display_light_menu_use_case)
    display_menu_thread = threading.Thread(target=display_menu, args=(display_menu_use_case,))
    display_menu_thread.start()



