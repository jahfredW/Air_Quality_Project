import datetime

from business.components.pollution_instant_high import PollutionInstant


class InstantService:
    def __init__(self, nom_ville):
        print("Initialisation du service de prévisions")
        self._pollution_ville = PollutionInstant(nom_ville)

    def previsions_all(self):
        data = self._pollution_ville.get_prev()
        data_dict = {
            'aqi': data.aqi,
            'co': data.co,
            'no': data.no,
            'no2': data.no2,
            'o3': data.o3,
            'so2': data.so2,
            'pm25': data.pm2_5,
            'pm10': data.pm10,
            'nh3': data.nh3
        }
        return data_dict



