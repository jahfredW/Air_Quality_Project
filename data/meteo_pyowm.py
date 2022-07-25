import datetime

import pyowm
import requests
from pyowm.utils.config import get_default_config
from pyowm.utils import measurables
import pollution_data

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
        liste_forecast = []
        pollution_dict = {}

        pollution = self._get_pollution_api()
        if pollution is not None:
            pol = pollution.city_id_registry()
            emplacements = pol.geopoints_for(ville)
            emplacement = emplacements[0]
            pol = pollution.airpollution_manager()
            print(emplacement.lon, emplacement.lat)
            forecast = pol.air_quality_forecast_at_coords(emplacement.lat, emplacement.lon)
            for f in forecast:
                pollution_dict[f.reference_time('date').date().isoformat()] = f.air_quality_data
            self.save_pollution_ville(ville, pollution_dict)
        else:
            raise Exception("Attention, l'API Pollution n'a pas été initialisée")

        return pollution_dict

    def save_pollution_ville(self, ville, forecast_dict):
        """
        enregistrement des prévisions de la ville en base de données
        :param ville: le nom de la ville
        :param forecast_dict : le dico de données de pollution
        :param forecast: les données de pollution
        :return: rien, alimente la base de données
        """
        if not pollution_data.ville_exists(ville):
            raise Exception("Save meteo ville : la ville n'a pas de correspondance")
        else:
            id_ville = pollution_data.get_id_ville(ville)[0][0]
            print(id_ville)

        pollution_data.delete_prevision_ville(ville)

        for date, values in forecast_dict.items():
            pollution_data.ajout_pollution_ville(values['aqi'],
                                                 values['co'], values['no'],
                                                 values['no2'], values['o3'],
                                                 values['so2'], values['pm2_5'], values['pm10'],
                                                 values['nh3'], date, datetime.date.today(),
                                                 id_ville)

        """
        liste_poluant = ['aqi', 'co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']

        prevision_jour = {}
        for item in liste_poluant:
            prevision_jour[item] = forecast.air_quality_data.get(item,'no_data')
        print(prevision_jour)

        pollution_data.ajout_pollution_ville(prevision_jour['aqi'], prevision_jour['co'],prevision_jour['no'], prevision_jour['no2'], prevision_jour['o3'],
                                             prevision_jour['so2'], prevision_jour['pm2_5'], prevision_jour['pm10'],
                                             prevision_jour['nh3'], datetime.date.today(), datetime.date.today(), id_ville)
        """


    #def get_pm2_5(self):



    def _need_refresh(self, ville):
        date_last_update = pollution_data.get_last_update(ville)

        if date_last_update is None:
            return True
        else:
            delta_heures = datetime.date.today() - date_last_update

            if delta_heures.days > 1:
                return True
            else:
                return False





p = PollutionPyown()
print(p.get_pollution_ville('Dunkerque'))

