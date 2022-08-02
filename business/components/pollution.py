from data.pollution_pyowm import PollutionPyown
import business.components.pollution_ville

class Pollution:
    def __init__(self):
        self._meteo_pyowm = PollutionPyown()
        self._meteo_villes = []

    def recherche_ville(self, nom_ville):
        return self._meteo_pyowm.get_ville(nom_ville)

    def get_pollution_ville(self, nom_ville):

        for pollution_ville in self._meteo_villes:
            if pollution_ville.ville.nom == nom_ville:
                return pollution_ville


        pollution = business.components.pollution_ville.PollutionVille(nom_ville)
        self._meteo_villes.append(pollution)

