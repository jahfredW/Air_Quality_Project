from presentation.web.views.pollution_ville_view import PollutionVilleView
from presentation.web.models.meteo_ville_model import PollutionVilleModel


class PollutionVilleController:

    def __init__(self):
        self._view = PollutionVilleView()
        self._model = None
        self.commentaire = ""

    def read_pollution_ville(self, nom_ville: str) -> str:
        self._model = PollutionVilleModel()
        self._view.nom_ville = nom_ville
        self._view._prevision_aqi = self._model._get_aqi(nom_ville)
        self._view._prevision_pm_2_5 = self._model._get_pm_2_5(nom_ville)
        self._view._prevision_pm_10 = self._model._get_pm10(nom_ville)
        self._view._prevision_so2 = self._model._get_so2(nom_ville)



        return self._view.render()


