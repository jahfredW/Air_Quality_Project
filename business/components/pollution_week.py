from business.entities.pollution_week_entitie import PollutionWeekEntitie
from business.entities.ville import Ville
from utils.meteo_common import MeteoCommon
from data.pollution_data import PollutionData
from data.pollution_pyowm import PollutionPyown
import datetime


class PollutionWeek:
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

    def init_pollution(self):

        need_refresh = self._need_refresh()

        if need_refresh:

            self._pollution_ville = self._pollution_pyown._get_week_pollution_week(self.ville.nom)

            if self._pollution_ville is not None:

                self.save_pollution_ville_by_date()

            else:
                raise Exception(
                    f"MeteoVille:_init_meteo: les données pour la ville {self.ville.nom} "
                    f"n'ont pas pu être initialisées via la librairie PyOWM.")

        else:
            self.load_pollution_ville()

    def get_prev(self):
        data = self.load_pollution_ville()

        return data

    def get_pm2_5(self):
        pm2_5_liste = []
        try:
            data = self.load_pollution_ville()
            for key, value in data.items():
                pm2_5_liste.append(value.pm2_5)
            return pm2_5_liste
        except:
            print("Les données pm2_5 sont indisponibles")

    def load_pollution_ville(self):
        pollution_ville = self._pollution_data.read_pollution_forecast_week(self.ville.nom)
        print(pollution_ville)

        if self.pollutions_liste:
            self.pollutions_liste.clear()

        for data in pollution_ville:
            prev_week = PollutionWeekEntitie()
            prev_week.ville = self.ville
            prev_week.period = data[0]
            prev_week.aqi = data[1]
            prev_week.co = data[2]
            prev_week.no = data[3]
            prev_week.no2 = data[4]
            prev_week.o3 = data[5]
            prev_week.so2 = data[6]
            prev_week.pm2_5 = data[7]
            prev_week.pm10 = data[8]
            prev_week.nh3 = data[9]
            prev_week.instant = data[10]
            prev_week.utc_time = data[11]

            self.pollutions_liste.append(prev_week)

    def save_pollution_ville_by_date(self):

        now = int(datetime.datetime.now().timestamp())

        forecast_dict = self._pollution_ville

        if not self._pollution_data.ville_exists(self.ville.nom):
            raise Exception("Save meteo ville : la ville n'a pas de correspondance")
        else:
            id_ville = self._pollution_data.get_id_ville(self.ville.nom)[0][0]

        self._pollution_data.delete_prevision_ville(self.ville.nom, "_week")

        print('Ajout des données en BDD:')

        for key, value in forecast_dict.items():

            for data in value:

                self._pollution_data.ajout_pollution_week_ville(now, datetime.datetime.today(), data[3]['aqi'],
                                                                data[3]['co'], data[3]['no'],
                                                             data[3]['no2'], data[3]['o3'],
                                                             data[3]['so2'], data[3]['pm2_5'],
                                                             data[3]['pm10'],
                                                             data[3]['nh3'], id_ville, key,  data[1],
                                                             )

    def _need_refresh(self):
        date_last_update = self._pollution_data.get_last_update(self.ville.nom, "_week")

        if date_last_update is None:
            return True

        else:
            delta_heures = datetime.date.today() - date_last_update

            if delta_heures.days > 1:
                return True
            else:
                return False


p = PollutionWeek('Calais')



