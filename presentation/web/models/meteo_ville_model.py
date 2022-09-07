from business.components.pollution import Pollution
from utils.meteo_common import MeteoCommon


class PollutionVilleModel:

    def __init__(self):
        self._pollution_ville = Pollution()

    def _get_aqi(self, nom_ville):
        aqi = self._pollution_ville.get_aqi(nom_ville)
        prev = {}

        for index in range(0, len(aqi)):
            prev[index] = aqi[index]

        print(prev)
        return prev

    def _get_pm10(self, nom_ville):
        pm10 = self._pollution_ville.get_pm10(nom_ville)
        prev = {}

        for index in range(0, len(pm10)):
            prev[index] = pm10[index]

        print(prev)
        return prev


    def _get_pm_2_5(self, nom_ville):
        pm25 = self._pollution_ville.get_pm_2_5(nom_ville)
        prev = {}

        for index in range(0, len(pm25)):
            prev[index] = pm25[index]

        print(prev)
        return prev

    def _get_so2(self, nom_ville):
        so2 = self._pollution_ville.get_so2(nom_ville)
        prev = {}

        for index in range(0, len(so2)):
            prev[index] = so2[index]

        print(prev)
        return prev
"""
    def _get_pm2_5(self, nom_ville):
        return self._pollution_ville.get_pm_2_5(nom_ville)

    def _get_pm10(self, nom_ville):
        return self._pollution_ville.get_pm10(nom_ville)

    def get_aqi_prev(self):
        prev = {}

        for index in range(0, len(self._get_aqi())):
            prev[index] = self._get_aqi()[index]

        print(prev)
        return prev

    def get_pm_2_5(self):
        prev = {}

        for index in range(0, len(self._get_pm2_5())):
            prev[index] = self._get_pm2_5()[index]

        return prev

    def get_pm10(self):
        prev = {}

        for index in range(0, len(self._get_pm10())):
            prev[index] = self._get_pm10()[index]

        return prev
"""






