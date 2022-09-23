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

        previsions = []

        maxi = len(indices)

        for day in range(len(indices)):
            dto = PollutionCardDTO()
            dto.period = day
            dto.indice = indices[day]

            previsions.append(dto)

        return previsions





