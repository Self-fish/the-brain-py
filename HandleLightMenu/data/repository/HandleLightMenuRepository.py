from Core.data.device.NoSerialException import NoSerialException
from HandleLightMenu.data.datasource import ApiDataSource
from HandleLightMenu.domain.model.LightMenuOptions import LightMenuOptions
from HandleLights.data.datasource.NoApiPreferencesException import NoApiPreferenceException


def update_light_preferences(menu_options: LightMenuOptions):
    if menu_options == LightMenuOptions.MANUAL_OFF:
        light_mode = "MANUAL_OFF"
    elif menu_options == LightMenuOptions.MANUAL_ON:
        light_mode = "MANUAL_ON"
    else:
        light_mode = "AUTOMATIC"
    try:
        return ApiDataSource.update_light_preferences(light_mode)
    except (NoApiPreferenceException, NoSerialException):
        return False
