import json
from datetime import datetime

import pyowm
from pyowm.utils.config import get_default_config

_meteo_already_exists = {}
_pollution_already_exists = {}


class PrevTabBuilder:
    def __init__(self, ville: str):
        self._data = PollutionPyown()
        self._prevs = self._data._get_pollution_ville(ville)
        self._data_list = []
        self._new_tab = []

    def tab_build(self):
        count_section = 1
        for prev in self._prevs:
            date_stamp = prev.ref_time
            date = datetime.fromtimestamp(prev.ref_time)
            date_str = str(date)
            self._new_tab.append((count_section, date_str, date_stamp, prev.air_quality_data))
            if date_str[11:] == "00:00:00":
                self._data_list.append(self._new_tab)
                self._new_tab = []
                count_section = 0
            count_section += 1

        print("récupération des données via l'API OWM")
        return self._data_list[0]


class PrevTabWeekBuilder:
    def __init__(self, ville: str):
        self._data = PollutionPyown()
        self._prevs = self._data._get_pollution_ville(ville)
        self._data_list = {}
        self._new_tab = []

    def tab_build(self):
        count_section = 1
        count_week = 0
        for prev in self._prevs:
            date_stamp = prev.ref_time
            date = datetime.fromtimestamp(prev.ref_time)
            date_str = str(date)
            self._new_tab.append((count_section, date_str, date_stamp, prev.air_quality_data))
            if date_str[11:] == "00:00:00":
                self._data_list[count_week] = (self._new_tab)
                self._new_tab = []
                count_section = 0
                count_week += 1
            count_section += 1

        print("récupération des données via l'API OWM")
        return self._data_list



class PollutionPyown:

    # ------------------------
    # Constructeur
    # ------------------------
    def __init__(self):
        self._apikey = 'de344c900509e22467e79e19be02d6bb'
        self._pollution_api_initialized = False
        self._pollution_api = None

        self._get_api()

    def _get_api(self):
        """
        vérification que l'initialisation n'a pas déjà été faite, pour ne pas faire des traitements inutiles
        :param
        :return: l'objet self._pollution_api
        """
        if not self._pollution_api_initialized:
            # on récupère le dico get_default_config dans la variable config_dict,
            config_dict = get_default_config()
            # modification du config_dict clé langage en fr:
            config_dict['language'] = 'fr'
            # création de l'objet _pollution_api
            self._pollution_api = pyowm.OWM(self._apikey, config_dict)
            # on passe l'initialisation à True
            self._pollution_api_initialized = True

        else:
            pass

        return self._pollution_api

    def get_ville(self, ville):
        """
        recherche les villes correspondant à la chaîne de caractère donnée en paramètre
        :param ville: chaîne de carcatère qui est le nom de la ville (ou une partie du nom)
        :return: liste des villes trouvées, liste vide si aucun résultat de recherche
        """
        pollution = self._get_api()
        if pollution is not None:
            reg = pollution.city_id_registry()
            villes = reg.ids_for(ville, country='FR', matching='like')
            new_dict = {}
            index = 0
            for ville in villes:
                if ville[1] not in new_dict.values():
                    new_dict[index] = ville[1]
                    index += 1
            return new_dict
        else:
            raise Exception("Attention, l'API Pollution n'a pas été initialisée")

    def _get_meteo_ville(self, ville):
        meteo_dict = {}
        """
        :param ville:
        :return: permet d'obtenir le dictionnaire des prévisions météo d'une ville
        """
        meteo = self._get_api()
        if meteo is not None:
            meteo_api_data = meteo.city_id_registry()
            location = meteo_api_data.geopoints_for(ville.lower())
            location = location[0]
            meteo_api_data = meteo.weather_manager()

            try:
                forecast = meteo_api_data.one_call(location.lat, location.lon, units='metrics')
                _meteo_already_exists[ville] = forecast
                return forecast

            except:
                print("Connexion à l'API indisponible pour le moment")

        else:
            raise Exception("Attention, l'API Pollution n'a pas été initialisée")

    def _get_pollution_ville(self, ville):
        """
        :param ville:
        :return l'objet pollution.py pour la ville:
        """

        pollution = self._get_api()
        if pollution is not None:
            pol = pollution.city_id_registry()
            try:
                emplacements = pol.geopoints_for(ville)
                emplacement = emplacements[0]
                print(emplacement)
            except:
                print("Erreur, la ville n'existe pas")
                return None
            try:
                pol = pollution.airpollution_manager()
                forecast = pol.air_quality_forecast_at_coords(emplacement.lat, emplacement.lon)
                return forecast

            except:
                print("Connexion à l'API indisponible pour le moment")

        else:
            raise Exception("Attention, l'API Pollution n'a pas été initialisée")




    def _get_instant_pollution_forecast(self, ville):
        forecast = PrevTabBuilder(ville).tab_build()
        return forecast


    def _get_week_pollution_week(self, ville):
        forecast = PrevTabWeekBuilder(ville).tab_build()
        return forecast


p = PrevTabWeekBuilder('Lille')
data = str(p.tab_build())

with open("test.txt", 'w') as t:
    json.dump(data, t)

with open("test.txt", 'w') as t:
    t.write(data)


