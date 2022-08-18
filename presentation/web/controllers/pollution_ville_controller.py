from presentation.web.views.pollution_ville_view import PollutionVilleView
from presentation.web.models.meteo_ville_model import PollutionVilleModel


class PollutionVilleController:

    def __init__(self):
        self._view = PollutionVilleView()
        self._model = None

    def read_pollution_ville(self, nom_ville: str) -> str:
        self._model = PollutionVilleModel(nom_ville)
        self._view.nom_ville = nom_ville
        self._view.previsions_aqi = self._model.get_aqi_prev()

        return self._view.render()
