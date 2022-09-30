from business.components.pollution_week_high import PollutionWeek


class ForecastService:
    def __init__(self, nom_ville):
        print("Initialisation du service de prévisions")
        self._pollution_ville = PollutionWeek(nom_ville)

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
