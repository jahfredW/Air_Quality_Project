from business.components.pollution import Pollution
from utils.meteo_common import MeteoCommon


class PollutionVilleModel:

    def __init__(self, nom_ville):
        self._ville = nom_ville
        self._pollution_ville = Pollution(nom_ville)
        self._aqi_description = Pollution.aqi_description((self.get_aqi())[0])

    def get_aqi(self):
        aqi = self._pollution_ville.get_aqi()
        prev = {}

        for index in range(0, len(aqi)):
            prev[index] = aqi[index]

        print(prev)
        return prev

    def get_pm10(self):
        pm10 = self._pollution_ville.get_pm10()
        prev = {}

        for index in range(0, len(pm10)):
            prev[index] = pm10[index]


        return prev


    def get_pm_2_5(self):
        pm25 = self._pollution_ville.get_pm_2_5()
        prev = {}

        for index in range(0, len(pm25)):
            prev[index] = pm25[index]


        return prev

    def get_so2(self):
        so2 = self._pollution_ville.get_so2()
        prev = {}

        for index in range(0, len(so2)):
            prev[index] = so2[index]


        return prev


    def get_aqi_description(self):
        return self._aqi_description


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






