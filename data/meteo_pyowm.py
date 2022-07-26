import datetime
import pyowm
import requests
from pyowm.utils.config import get_default_config
from pyowm.utils import measurables
import pollution_data

_meteo_already_exists = {}
_pollution_already_exists = {}

class PollutionPyown:

    #------------------------
    #Constructeur
    #------------------------
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
            new_list = []
            for ville in villes:
                if ville[1] not in new_list:
                    new_list.append(ville[1])
            return new_list
        else:
            raise Exception("Attention, l'API Pollution n'a pas été initialisée")


    def get_meteo_ville(self,ville):
        meteo_dict = {}
        """
        :param ville:
        :return: permet d'obtenir le dictionnaire des prévisions météo d'une ville
        """

        if ville in _meteo_already_exists:
            return _meteo_already_exists[ville]

        else:
            meteo = self._get_api()
            if meteo is not None:
                meteo_api_data = meteo.city_id_registry()
                location = meteo_api_data.geopoints_for(ville)
                location = location[0]
                meteo_api_data = meteo.weather_manager()

                try:
                    forecast = meteo_api_data.one_call(location.lat, location.lon, units='metrics')
                    _meteo_already_exists[ville] = forecast


                except:
                    print("Connexion à l'API indisponible pour le moment")

            else:
                raise Exception("Attention, l'API Pollution n'a pas été initialisée")


    def _get_pollution_ville(self, ville):
        """
        :param ville:
        :return l'objet pollution pour la ville:
        """
        liste_forecast = []
        pollution_dict = {}

        if ville in _pollution_already_exists:
            return _pollution_already_exists[ville]

        else:
            pollution = self._get_api()
            if pollution is not None:
                pol = pollution.city_id_registry()
                emplacements = pol.geopoints_for(ville)
                emplacement = emplacements[0]
                pol = pollution.airpollution_manager()

                try:
                    forecast = pol.air_quality_forecast_at_coords(emplacement.lat, emplacement.lon)
                    _meteo_already_exists[ville] = forecast
                    self.save_pollution_ville(ville, forecast)
                    return forecast

                except:
                    print("Connexion à l'API indisponible pour le moment")

            else:
                raise Exception("Attention, l'API Pollution n'a pas été initialisée")

    def _read_pollution_ville(self, ville):
        pollution_dict = {}

        data_pollution_ville = pollution_data.read_pollution_forecast(ville)

        for previsions in data_pollution_ville:
            pollution_daily = {}
            pollution_daily['date'] = previsions[0]
            pollution_daily['aqi'] = previsions[1]
            pollution_daily['co'] = previsions[2]
            pollution_daily['no'] = previsions[3]
            pollution_daily['no2'] = previsions[4]
            pollution_daily['o3'] = previsions[5]
            pollution_daily['so2'] = previsions[6]
            pollution_daily['pm2_5'] = previsions[7]
            pollution_daily['pm10'] = previsions[8]
            pollution_daily['nh3'] = previsions[9]

            pollution_dict[pollution_daily['date']] = pollution_daily


    def save_pollution_ville(self, ville, forecast):
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

        pollution_data.delete_prevision_ville(ville)

        forecast_dict = {}
        for f in forecast:
            forecast_dict[f.reference_time('date').date().isoformat()] = f.air_quality_data

        for date, values in forecast_dict.items():
            pollution_data.ajout_pollution_ville(values['aqi'],
                                                 values['co'], values['no'],
                                                 values['no2'], values['o3'],
                                                 values['so2'], values['pm2_5'], values['pm10'],
                                                 values['nh3'], date, datetime.date.today(),
                                                 id_ville)


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


    def get_prevision_pollution(self, ville):

        need_refresh = self._need_refresh(ville)

        if need_refresh:
            pollution_dict = {}
            pollution_forecast = self._get_pollution_ville(ville)
            for f in pollution_forecast:
                pollution_dict[f.reference_time('date').date().isoformat()] = f.air_quality_data
            return pollution_dict

        else:
            data_bdd = self._read_pollution_ville(ville)
            return data_bdd




p = PollutionPyown()
p.get_prevision_pollution('Paris')

