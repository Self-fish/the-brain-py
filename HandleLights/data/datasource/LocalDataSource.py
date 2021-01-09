from HandleLights.data.datamodel.LightPreferencesDataModel import LightPreferencesDataModel
from HandleLights.domain.model.LightMode import LightMode


def get_light_preferences():
    return LightPreferencesDataModel("15:00", "23:00", LightMode.AUTOMATIC)
