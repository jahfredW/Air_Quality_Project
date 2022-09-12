from utils.meteo_common import *
from utils.meteo_utils import MeteoUtils


class UIHelper:

    @staticmethod
    def icon_from_weather_status(weather_status: str) -> str:
        if weather_status == MeteoCommon.STATUT_API_NUAGEUX:
            return "fa-clouds"
        elif weather_status == MeteoCommon.STATUT_API_PARTIELLEMENT_NUAGEUX:
            return "fa-cloud"
        elif weather_status == MeteoCommon.STATUT_API_PEU_NUAGEUX:
            return "fa-cloud-sun"
        elif weather_status == MeteoCommon.STATUT_API_CIEL_DEGAGE:
            return "fa-sun"
        elif weather_status == MeteoCommon.STATUT_API_LEGERE_PLUIE:
            return "fa-cloud-drizzle"
        elif weather_status == MeteoCommon.STATUT_API_BRUME:
            return "fa-cloud-fog"
        else:
            return "seal-question"

    @staticmethod
    def day_of_the_week_from_period(period: int) -> str:
        day = MeteoUtils.get_jour_from_period(period).strftime("%A")

        if day == "Monday":
            return "Lundi"
        if day == "Tuesday":
            return "Mardi"
        if day == "Wednesday":
            return "Mercredi"
        if day == "Thursday":
            return "Jeudi"
        if day == "Friday":
            return "Vendredi"
        if day == "Saturday":
            return "Samedi"
        if day == "Sunday":
            return "Dimanche"
