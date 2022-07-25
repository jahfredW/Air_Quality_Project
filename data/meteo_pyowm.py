import pyowm
import requests
from pyowm.utils.config import get_default_config
from pyowm.utils import measurables

class PollutionPyown:
    #------------------------
    #Constructeur
    #------------------------
    def __init__(self):
        self._apikey = 'de344c900509e22467e79e19be02d6bb'
        self._pollution_api_initialized = False
        self._pollution_api = None

        self._get_pollution_api()

    def _get_pollution_api(self):
        """
        vérification que l'initialisation n'a pas déjà été faite, pour ne pas faire des traitements inutiles
        :param
        :return: l'objet self._pollution_api
        """
        if not self._pollution_api_initialized:
            #on récupère le dico get_default_config dans la variable config_dict,
            config_dict = get_default_config()
            #modification du config_dict clé langage en fr:
            config_dict['language'] = 'fr'
            #création de l'objet _pollution_api
            self._pollution_api = pyowm.OWM(self._apikey, config_dict)
            #on passe l'initialisation à True
            self._pollution_api_initialized = True

        else:
            pass

        return self._pollution_api

    def get_meteo_ville(self, ville):
        """
        recherche les villes correspondant à la chaîne de caractère donnée en paramètre
        :param ville: chaîne de carcatère qui est le nom de la ville (ou une partie du nom)
        :return: liste des villes trouvées, liste vide si aucun résultat de recherche
        """
        pollution = self._get_pollution_api()
        if pollution is not None:
            reg = pollution.city_id_registry()
            villes = reg.ids_for(ville, country='FR', matching='like')
            new_list = []
            for ville in villes:
                if ville[1] not in new_list:
                    new_list.append(ville[1])
            return new_list
        else:
            raise Exception("Attention, l'API Pollution n'a pas été initialisée")

    def get_pollution_ville(self, ville):
        """
        :param ville:
        :return l'objet pollution pour la ville:
        """
        pollution = self._get_pollution_api()
        if pollution is not None:
            pol = pollution.city_id_registry()
            emplacements = pol.geopoints_for(ville)
            emplacement = emplacements[0]
            pol = pollution.airpollution_manager()
            print(emplacement.lon, emplacement.lat)
            forecast = pol.air_quality_at_coords(emplacement.lat, emplacement.lon)
        else:
            raise Exception("Attention, l'API Pollution n'a pas été initialisée")

        return forecast.air_quality_data


p = PollutionPyown()
print(p.get_pollution_ville('Lille'))

