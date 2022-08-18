from business.entities.pollution import Pollution
from business.entities.ville import Ville
from utils.meteo_common import MeteoCommon
from data.pollution_data import PollutionData
from data.pollution_pyowm import PollutionPyown
import datetime


class PollutionVille:
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
        self._pollution_pyown = PollutionPyown() #classe d'accès aux données en API
        self._pollution_data = PollutionData() #classe d'acces au données en BDD
        self._pollution_ville = None
        self.pollutions = {}

        self._init_meteo() #initialisation des données de la classe avec les infos pollution de la ville

    @property
    def ville(self):
        return self._ville

    @ville.setter
    def ville(self, value):
        self._ville = value

    # ---------------
    # méthodes
    # ---------------

    # implémentation de la méthode d'initialisation
    def _init_meteo(self):
        #besoin de refresh ?
        need_refresh = self._need_refresh()

        if need_refresh:
            #si oui, on récupère les données via l'api distante
            self._pollution_ville = self._pollution_pyown._get_pollution_ville(self.ville.nom)
            print(self._pollution_ville)
            #si les données existes, on va créer une série d'objets de type pollution
            if self._pollution_ville is not None:
                period = 0
                for f in self._pollution_ville:
                    pollution = Pollution()
                    pollution.ville = self.ville
                    pollution.day = f.reference_time('date').date().isoformat()
                    pollution.aqi = f.air_quality_data.get('aqi', None)
                    pollution.co = f.air_quality_data.get('co', None)
                    pollution.no = f.air_quality_data.get('no', None)
                    pollution.no2 = f.air_quality_data.get('no2', None)
                    pollution.o3 = f.air_quality_data.get('o3', None)
                    pollution.so2 = f.air_quality_data.get('so2', None)
                    pollution.pm2_5 = f.air_quality_data.get('pm2_5', None)
                    pollution.pm10 = f.air_quality_data.get('pm10', None)
                    pollution.nh3 = f.air_quality_data.get('nh3', None)

                    #Qu'on stocke dans le dictionnaire self.pollutions en fonction de la période
                    self.pollutions[period] = pollution

                    period += 1
                    print(pollution.ville, pollution.day, pollution.pm2_5, pollution.pm10)
                    print(len(self._pollution_ville))
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
        aqi = self.load_pollution_ville()
        for key, value in aqi.items():
            aqi_liste.append(value.aqi)
        return aqi_liste


    def load_pollution_ville(self):
        pollution_ville = self._pollution_data.read_pollution_forecast(self.ville.nom)
        self.pollutions.clear()

        period = 0

        for prev in pollution_ville:
            prev_jour = Pollution()
            prev_jour.ville = self.ville
            prev_jour.day = prev[0]
            prev_jour.aqi = prev[1]
            prev_jour.co = prev[2]
            prev_jour.no = prev[3]
            prev_jour.no2 = prev[4]
            prev_jour.o3 = prev[5]
            prev_jour.so2 = prev[6]
            prev_jour.pm2_5 = prev[7]
            prev_jour.pm10 = prev[8]
            prev_jour.nh3 = prev[9]


            self.pollutions[period] = prev_jour
            print(prev)
            period += 1
        return self.pollutions



    def save_pollution_ville_by_date(self):

        forecast_dict = {}
        # Ici on save les données bruts récupérées via l'API
        # En fonction de la date ( donc forcément une prev par jour)
        for f in self._pollution_ville:
            forecast_dict[f.reference_time('date').date().isoformat()] = f.air_quality_data

        """
        for index in range(len(self._pollution_ville)):
            forecast_dict[index] = self._pollution_ville[index]
        """

        if not self._pollution_data.ville_exists(self.ville.nom):
            raise Exception("Save meteo ville : la ville n'a pas de correspondance")
        else:
            id_ville = self._pollution_data.get_id_ville(self.ville.nom)[0][0]

        self._pollution_data.delete_prevision_ville(self.ville.nom)



        print('Ajout des données en BDD:')
        for day, values in forecast_dict.items():
            self._pollution_data.ajout_pollution_ville(values['aqi'],
                                                 values['co'], values['no'],
                                                 values['no2'], values['o3'],
                                                 values['so2'], values['pm2_5'], values['pm10'],
                                                 values['nh3'], day, datetime.datetime.today(),
                                                 id_ville)

    def _need_refresh(self):
        date_last_update = self._pollution_data.get_last_update(self.ville.nom)

        if date_last_update is None:
            return True

        else:
            delta_heures = datetime.date.today() - date_last_update

            if delta_heures.days > 1:
                return True
            else:
                return False




