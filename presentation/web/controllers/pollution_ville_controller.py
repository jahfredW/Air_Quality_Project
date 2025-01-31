from presentation.web.views.pollution_ville_view import PollutionVilleView
from presentation.web.models.meteo_ville_model import PollutionVilleModel


class PollutionVilleController:

    def __init__(self):
        self._view = PollutionVilleView()
        self._model = None
        self.commentaire = ""

    def read_pollution_ville(self, nom_ville: str) -> str:
        self._model = PollutionVilleModel(nom_ville)
        self._view.nom_ville = nom_ville
        self._view._prevision_aqi = self._model.get_aqi()
        self._view._prevision_pm_2_5 = self._model.get_pm_2_5()
        self._view._prevision_pm_10 = self._model.get_pm10()
        self._view._prevision_so2 = self._model.get_so2()



        return self._view.render()


