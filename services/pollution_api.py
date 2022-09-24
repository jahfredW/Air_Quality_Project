from utils.configuration import Configuration
from business.components.pollution import Pollution
from services.prevision_service import PrevisionsService
from services.dto.pollution_card_dto import PollutionCardDTO


class PollutionAPI:

    @staticmethod
    def get_environment():
        environment = (Configuration().get_instance().version,
                       Configuration().get_instance().target)

        return {
            "version": environment[0],
            "target": environment[1],
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





