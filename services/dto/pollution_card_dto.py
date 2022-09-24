import jsons
from services.dto.dto_base import DTO_base

class PollutionCardDTO(DTO_base):
    def __init__(self):
        self.period = -1
        self.indice = -1
        self.pm2_5 = -1
        self.description = ""

