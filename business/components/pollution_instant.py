from business.entities.pollution_instant import Pollution_instant
from business.entities.ville import Ville
from utils.meteo_common import MeteoCommon
from data.pollution_data import PollutionData
from data.pollution_pyowm import PollutionPyown
import datetime


class PollutionForecast:
    """
    Sert à récupérer les données correspondant au nom de la ville
    Soit via l'API, soit via la BBD.
    Inscrit les données dans self._pollution_ville ( données brut)
    Crée un dictionnaire self.pollutions avec les prévisions par période :
    C'est un dictionnaire d'objets Pollution
    Ici on ne fait que récupérer les données et construire les objets correspondant

    """

    def __init__(self, nom_ville):
        self.ville = Ville()
        self.ville.nom = nom_ville
        self._pollution_pyown = PollutionPyown()  # classe d'accès aux données en API
        self._pollution_data = PollutionData()  # classe d'acces au données en BDD
        self._pollution_ville = None
        self.pollutions_liste = []
        self.prev_jour = None
        self.init_pollution()  # initialisation des données de la classe avec les infos pollution de la ville

    @property
    def ville(self):
        return self._ville

    @ville.setter
    def ville(self, value):
        self._ville = value

    @staticmethod
    def transform_date(dateFormat):
        date = "-".join(list(reversed(dateFormat[5:10].split('-'))))
        return date

    # ---------------
    # méthodes
    # ---------------

    # implémentation de la méthode d'initialisation
    def init_pollution(self):

        need_refresh = self._need_refresh()

        if need_refresh:
            pollutions = {}
            # besoin de refresh ?
            index = 0
            # si oui, on récupère les données via l'api distante
            self._pollution_ville = self._pollution_pyown._get_instant_pollution_forecast(self.ville.nom)
            # si les données existes, on va créer une série d'objets de type pollution
            if self._pollution_ville is not None:

                pollution = Pollution_instant()
                pollution.instant = self._pollution_ville[0][2]
                pollution.ville = self.ville
                pollution.aqi = self._pollution_ville[0][3]['aqi']
                pollution.co = self._pollution_ville[0][3]['co']
                pollution.no = self._pollution_ville[0][3]['no']
                pollution.no2 = self._pollution_ville[0][3]['no2']
                pollution.o3 = self._pollution_ville[0][3]['o3']
                pollution.so2 = self._pollution_ville[0][3]['so2']
                pollution.pm2_5 = self._pollution_ville[0][3]['pm2_5']
                pollution.pm10 = self._pollution_ville[0][3]['pm10']
                pollution.nh3 = self._pollution_ville[0][3]['nh3']

                print(pollution.aqi, pollution.co, pollution.o3)



                # Qu'on stocke dans le dictionnaire self.pollutions en fonction de la période
                # self.pollutions[period] = pollution

                # period += 1
                # print(pollution.ville, pollution.day, pollution.pm2_5, pollution.pm10)
                # print(len(self._pollution_ville))
                # On sauvegarde les données brut dans la base de données
                self.save_pollution_ville_by_date()


            else:
                raise Exception(
                    f"MeteoVille:_init_meteo: les données pour la ville {self.ville.nom} n'ont pas pu être initialisées via la librairie PyOWM.")
                return None

        else:
            self.load_pollution_ville()

    # fonction de récupération, ne sert pas à consulter les données mais à construire les objets
    # Ne sert pas ici
    def get_aqi(self):

        aqi_liste = []
        data = self.load_pollution_ville()
        for key, value in data.items():
            aqi_liste.append(value.aqi)
        return aqi_liste

    def get_pm2_5(self):
        pm2_5_liste = []
        try:
            data = self.load_pollution_ville()
            for key, value in data.items():
                pm2_5_liste.append(value.pm2_5)
            return pm2_5_liste
        except:
            print("Les données pm2_5 sont indisponibles")

    def get_pm10(self):
        pm10_liste = []
        try:
            data = self.load_pollution_ville()
            for key, value in data.items():
                pm10_liste.append(value.pm10)
            return pm10_liste
        except:
            print("Les données pm10 sont indisponibles ")

    def get_so2(self):
        so2_liste = []
        try:
            data = self.load_pollution_ville()
            for value in data.values():
                so2_liste.append(value.so2)
            return so2_liste
        except:
            print("Les données pm10 sont indisponibles ")

    def load_pollution_ville(self):
        pollution_ville = self._pollution_data.read_pollution_forecast_daily(self.ville.nom)
        pol = pollution_ville[0]

        if self.prev_jour:
            self.prev_jour.clear()

        prev_jour = Pollution_instant()
        prev_jour.ville = self.ville
        prev_jour.instant = pol[0]
        prev_jour.aqi = pol[1]
        prev_jour.co = pol[2]
        prev_jour.no = pol[3]
        prev_jour.no2 = pol[4]
        prev_jour.o3 = pol[5]
        prev_jour.so2 = pol[6]
        prev_jour.pm2_5 = pol[7]
        prev_jour.pm10 = pol[8]
        prev_jour.nh3 = pol[9]

        self.prev_jour = prev_jour
        return self.prev_jour


    def save_pollution_ville_by_date(self):

        now = int(datetime.datetime.utcnow().timestamp())
        forecast_dict = {}
        # Ici on save les données bruts récupérées via l'API
        # En fonction de la date ( donc forcément une prev par jour)

        forecast_dict = self._pollution_ville[0][3]

        if not self._pollution_data.ville_exists(self.ville.nom):
            raise Exception("Save meteo ville : la ville n'a pas de correspondance")
        else:
            id_ville = self._pollution_data.get_id_ville(self.ville.nom)[0][0]
            print(id_ville)

        self._pollution_data.delete_prevision_ville(self.ville.nom)

        print('Ajout des données en BDD:')

        self._pollution_data.ajout_pollution_daily_ville(forecast_dict['aqi'], forecast_dict['co'], forecast_dict['no'],
                                                         forecast_dict['no2'], forecast_dict['o3'],
                                                         forecast_dict['so2'], forecast_dict['pm2_5'],
                                                         forecast_dict['pm10'],
                                                         forecast_dict['nh3'], now, datetime.datetime.today(),
                                                         id_ville)

    def _need_refresh(self):
        hour_last_update = self._pollution_data.get_last_update_daily(self.ville.nom)

        now = int(datetime.datetime.utcnow().timestamp())

        if hour_last_update is None:
            return True

        else:
            delta_hour = hour_last_update - now

            if delta_hour >= 3600:
                return True
            else:
                return False

