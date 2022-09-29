from business.components.pollution_forecast import PollutionForecast


class ForecastService:
    def __init__(self, nom_ville):
        print("Initialisation du service de prévisions")
        self._pollution_ville = PollutionForecast(nom_ville)

    def previsions_all(self):
        data = self._pollution_ville.pollutions_liste
        return data

    def previsions_co_jour(self):
        prev_jour_co = {}
        data = self._pollution_ville.pollutions_liste
        prev_jour = data[0]
        for key, value in prev_jour.items():
            prev_jour_co[key] = value.co
        return prev_jour_co

    def previsions_aqi_jour(self):
        prev_jour_aqi = {}
        data = self._pollution_ville.pollutions_liste
        prev_jour = data[0]
        for key, value in prev_jour.items():
            prev_jour_aqi[key] = value.aqi
        return prev_jour_aqi

    def previsions_so2_jour(self):
        prev_jour_so2 = {}
        data = self._pollution_ville.pollutions_liste
        prev_jour = data[0]
        for key, value in prev_jour.items():
            prev_jour_so2[key] = value.so2
        return prev_jour_so2

    def previsions_nh3_jour(self):
        prev_jour_nh3 = {}
        data = self._pollution_ville.pollutions_liste
        prev_jour = data[0]
        for key, value in prev_jour.items():
            prev_jour_nh3[key] = value.nh3
        return prev_jour_nh3

    def previsions_no_jour(self):
        prev_jour_no = {}
        data = self._pollution_ville.pollutions_liste
        prev_jour = data[0]
        for key, value in prev_jour.items():
            prev_jour_no[key] = value.no
        return prev_jour_no

    def previsions_no2_jour(self):
        prev_jour_no2 = {}
        data = self._pollution_ville.pollutions_liste
        prev_jour = data[0]
        for key, value in prev_jour.items():
            prev_jour_no2[key] = value.no2
        return prev_jour_no2

    def previsions_o3_jour(self):
        prev_jour_o3 = {}
        data = self._pollution_ville.pollutions_liste
        prev_jour = data[0]
        for key, value in prev_jour.items():
            prev_jour_o3[key] = value.o3
        return prev_jour_o3

    def previsions_pm25_jour(self):
        prev_jour_pm25 = {}
        data = self._pollution_ville.pollutions_liste
        prev_jour = data[0]
        for key, value in prev_jour.items():
            prev_jour_pm25[key] = value.pm2_5
        return prev_jour_pm25

    def previsions_pm10_jour(self):
        prev_jour_pm10 = {}
        data = self._pollution_ville.pollutions_liste
        prev_jour = data[0]
        for key, value in prev_jour.items():
            prev_jour_pm10[key] = value.pm10
        return prev_jour_pm10