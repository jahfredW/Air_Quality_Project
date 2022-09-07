from data.pollution_pyowm import PollutionPyown
import business.components.pollution_ville


class Pollution:
    """
    Dans cette classe, on récupère les données de pollution_ville (classe PollutionVille)
    Récupération des données contenues dans les objets créés par pollution_ville.
    """

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

        return pollution

    def get_aqi(self, nom_ville):
        pollution = self.get_pollution_ville(nom_ville)
        return pollution.get_aqi()

    def get_pm10(self, nom_ville):
        pollution = self.get_pollution_ville(nom_ville)
        return pollution.get_pm10()

    def get_pm_2_5(self, nom_ville):
        pollution = self.get_pollution_ville(nom_ville)
        return pollution.get_pm2_5()

    def get_so2(self, nom_ville):
        pollution = self.get_pollution_ville(nom_ville)
        return pollution.get_so2()




