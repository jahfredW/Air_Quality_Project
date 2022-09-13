from presentation.web.views.pollution_ville_bulma_view import PollutionVilleBulmaView
from presentation.web.models.meteo_ville_model import PollutionVilleModel


class PollutionVilleBulmaController:

    def __init__(self):
        self._view = PollutionVilleBulmaView()
        self._model = None

    def read_pollution_ville(self, nom_ville: str) -> str:
        self._model = PollutionVilleModel(nom_ville)
        self._view.nom_ville = nom_ville
        self._view.aqi_jour = self._model.get_aqi()
        self._view.pm10_jour = self._model.get_pm10()
        self._view.pm25_jour = self._model.get_pm_2_5()
        self._view.so2_jour = self._model.get_so2()
        self._view.previsions_description = self._model.get_aqi_description()

        return self._view.render()
