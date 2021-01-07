from HandleLights.domain.model.LightPreferencesSource import LightPreferencesSource


class LightPreferences:

    def __init__(self, starting_hour, finishing_hour, source: LightPreferencesSource):
        self.starting_hour = starting_hour
        self.finishing_hour = finishing_hour
        self.source = source

