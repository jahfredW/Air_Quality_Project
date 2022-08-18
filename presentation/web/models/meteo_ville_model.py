from business.components.pollution_ville import PollutionVille
from utils.meteo_common import MeteoCommon

class PollutionVilleModel:

    def __init__(self, nom_ville):
        self._pollution_ville = PollutionVille(nom_ville)

    def _get_aqi(self):
        return self._pollution_ville.get_aqi()


    def get_aqi_prev(self):
        prev = {}

        prev[MeteoCommon.PREVISION_AUJOURDHUI] = self._get_aqi()[MeteoCommon.PREVISION_AUJOURDHUI]
        prev[MeteoCommon.PREVISION_J_PLUS_1] = self._get_aqi()[MeteoCommon.PREVISION_J_PLUS_1]
        prev[MeteoCommon.PREVISION_J_PLUS_2] = self._get_aqi()[MeteoCommon.PREVISION_J_PLUS_2]
        prev[MeteoCommon.PREVISION_J_PLUS_3] = self._get_aqi()[MeteoCommon.PREVISION_J_PLUS_3]
        prev[MeteoCommon.PREVISION_J_PLUS_4] = self._get_aqi()[MeteoCommon.PREVISION_J_PLUS_4]
        prev[MeteoCommon.PREVISION_J_PLUS_5] = self._get_aqi()[MeteoCommon.PREVISION_J_PLUS_5]

        return prev

