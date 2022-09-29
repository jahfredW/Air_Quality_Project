import datetime

import pyowm
from pyowm.utils.config import get_default_config


_meteo_already_exists = {}
_pollution_already_exists = {}


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

    def get_pollution_ville(self, ville):
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
                #f = pol.ozone_around_coords(emplacement.lat, emplacement.lon)
                return forecast

            except:
                print("Connexion à l'API indisponible pour le moment")

        else:
            raise Exception("Attention, l'API Pollution n'a pas été initialisée")


p = PollutionPyown()
prevs = p.get_pollution_ville('Dunkerque')
count_section = 0
count_day = 0
new_tab = []
data_list = []

for prev in prevs:

    date = datetime.datetime.fromtimestamp(prev.ref_time)
    print(date)

    date_str = str(date)
    new_tab.append((count_section, date_str))

    if date_str[11:] == "00:00:00":
        data_list.append(new_tab)
        new_tab = []
        count_section = 0
    count_section += 1

print(data_list)



class prevTabBuilder:
    def __init__(self, ville: str):
        self._data = PollutionPyown()
        self._prevs = self._data.get_pollution_ville(ville)
        self._data_list = []
        self._new_tab = []

    def tab_build(self):
        count_section = 1
        for prev in self._prevs:
            date = datetime.datetime.fromtimestamp(prev.ref_time)
            date_str = str(date)
            self._new_tab.append((count_section, date_str, prev.air_quality_data))
            if date_str[11:] == "00:00:00":
                self._data_list.append(self._new_tab)
                self._new_tab = []
                count_section = 0
            count_section += 1

        return self._data_list

p = prevTabBuilder('Lille')
print(p.tab_build())




