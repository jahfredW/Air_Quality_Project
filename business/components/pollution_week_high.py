import business.components.pollution_instant_to_back
from data.pollution_pyowm import PollutionPyown
from business.components.pollution_week import PollutionWeek


class PollutionWeek:
    """
    Dans cette classe, on récupère les données de pollution_ville (classe PollutionVille)
    Récupération des données contenues dans les objets créés par pollution_ville.
    """

    def __init__(self, nom_ville):
        self._meteo_pyowm = PollutionPyown()
        self._meteo_villes = []
        self._ville = nom_ville

    def recherche_ville(self, nom_ville):
        return self._meteo_pyowm.get_ville(nom_ville)

    def get_pollution_instant_ville(self):

        for pollution_ville in self._meteo_villes:
            if pollution_ville.ville.nom == self._ville:
                return pollution_ville

        pollution = business.components.pollution_week.PollutionWeek(self._ville)
        self._meteo_villes.append(pollution)

        return pollution

    def get_prev(self):
        pollution = business.components.pollution_instant_to_back.PollutionForecast(self._ville)
        return pollution.get_prev()