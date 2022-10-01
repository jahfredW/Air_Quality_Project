import datetime

from services.dto.PollutionForecastDTO import PollutionForecastDTO
from utils.configuration import Configuration
from business.components.pollution import Pollution
from services.prevision_service import PrevisionsService
from services.forecast_service import ForecastService
from services.instant_service import InstantService
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
    def get_previsions_instant(ville: str):
        ville = ville.replace('+', ' ')
        service = InstantService(ville)
        print("service de prévisions initialisé")

        previsions = []

        dto = PollutionForecastDTO()
        dto.aqi = service.previsions_all()['aqi']
        dto.co = service.previsions_all()['co']
        dto.so2 = service.previsions_all()['so2']
        dto.nh3 = service.previsions_all()['nh3']
        dto.no = service.previsions_all()['no']
        dto.no2 = service.previsions_all()['no2']
        dto.o3 = service.previsions_all()['o3']
        dto.pm25 = service.previsions_all()['pm25']
        dto.pm10 = service.previsions_all()['pm10']

        previsions.append(dto)

        return previsions

