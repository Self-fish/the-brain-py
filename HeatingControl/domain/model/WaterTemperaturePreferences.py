from HeatingControl.domain.model.WaterTemperaturePreferencesSource import WaterTemperaturePreferencesSource


class WaterTemperaturePreferences:

    def __init__(self, temperature, source: WaterTemperaturePreferencesSource):
        self.temperature = temperature
        self.source = source
