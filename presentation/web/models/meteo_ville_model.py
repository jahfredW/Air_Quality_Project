from business.components.pollution_ville import PollutionVille
from utils.meteo_common import MeteoCommon

class PollutionVilleModel:

    def __init__(self, nom_ville):
        self._pollution_ville = PollutionVille(nom_ville)

    def _get_aqi(self):
        return self._pollution_ville.get_aqi()


    def _get_pm2_5(self):
        return self._pollution_ville.get_pm2_5()


    def get_aqi_prev(self):
        prev = {}

        prev[MeteoCommon.PREVISION_AUJOURDHUI] = self._get_aqi()[MeteoCommon.PREVISION_AUJOURDHUI]
        prev[MeteoCommon.PREVISION_J_PLUS_1] = self._get_aqi()[MeteoCommon.PREVISION_J_PLUS_1]
        prev[MeteoCommon.PREVISION_J_PLUS_2] = self._get_aqi()[MeteoCommon.PREVISION_J_PLUS_2]
        prev[MeteoCommon.PREVISION_J_PLUS_3] = self._get_aqi()[MeteoCommon.PREVISION_J_PLUS_3]
        prev[MeteoCommon.PREVISION_J_PLUS_4] = self._get_aqi()[MeteoCommon.PREVISION_J_PLUS_4]

        return prev


    def get_pm_2_5(self):
        prev2 = {}

        prev2[MeteoCommon.PREVISION_AUJOURDHUI] = self._get_pm2_5()[MeteoCommon.PREVISION_AUJOURDHUI]
        prev2[MeteoCommon.PREVISION_J_PLUS_1] = self._get_pm2_5()[MeteoCommon.PREVISION_J_PLUS_1]
        prev2[MeteoCommon.PREVISION_J_PLUS_2] = self._get_pm2_5()[MeteoCommon.PREVISION_J_PLUS_2]
        prev2[MeteoCommon.PREVISION_J_PLUS_3] = self._get_pm2_5()[MeteoCommon.PREVISION_J_PLUS_3]
        prev2[MeteoCommon.PREVISION_J_PLUS_4] = self._get_pm2_5()[MeteoCommon.PREVISION_J_PLUS_4]


        return prev2


