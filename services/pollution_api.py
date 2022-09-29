from services.dto.PollutionForecastDTO import PollutionForecastDTO
from utils.configuration import Configuration
from business.components.pollution import Pollution
from services.prevision_service import PrevisionsService
from services.forecast_service import ForecastService
from services.dto.pollution_card_dto import PollutionCardDTO


class PollutionAPI:

    @staticmethod
    def get_environment():
        environment = [Configuration().get_instance().version,
                       Configuration().get_instance().target,
                       Configuration().get_instance().name]

        return {
            "version": environment[0],
            "env": environment[1],
            "name": environment[2],
        }

    @staticmethod
    def get_previsions(ville: str):
        ville = ville.replace('+', ' ')
        service = PrevisionsService(ville)
        print("service de prévisions initialisé")
        indices = service.previsions_indice()
        pm_2_5 = service.previsions_pm2_5()
        description = service.previsions_status()


        previsions = []

        maxi = len(indices)

        if maxi >= 7:
            maxi = 7

        for day in range(maxi):
            dto = PollutionCardDTO()
            dto.period = day
            dto.indice = indices[day]
            dto.pm2_5 = pm_2_5[day]
            dto.description = description[day]

            previsions.append(dto)

        return previsions


    @staticmethod
    def get_previsions_jour(ville: str):
        ville = ville.replace('+', ' ')
        service = ForecastService(ville)
        print("service de prévisions initialisé")
        aqi = service.previsions_aqi_jour()
        co = service.previsions_co_jour()
        so2 = service.previsions_so2_jour()
        nh3 = service.previsions_nh3_jour()
        no = service.previsions_no_jour()
        no2 = service.previsions_no2_jour()
        o3 = service.previsions_o3_jour()
        pm25 = service.previsions_pm25_jour()
        pm10 = service.previsions_pm10_jour()


        previsions = []

        maxi = len(aqi)

        for hour in range(maxi):
            dto = PollutionForecastDTO()
            dto.period = hour
            dto.aqi = aqi[hour]
            dto.co = co[hour]
            dto.so2 = so2[hour]
            dto.nh3 = nh3[hour]
            dto.no = no[hour]
            dto.no2 = no2[hour]
            dto.o3 = o3[hour]
            dto.pm25 = pm25[hour]
            dto.pm10 = pm10[hour]

            previsions.append(dto)

        return previsions


