import jsons
from services.dto.dto_base import DTO_base

class PollutionForecastDTO(DTO_base):
    def __init__(self):
        self.period = -1
        self.co = -1
        self.aqi = -1
        self.so2 = -1
        self.nh3 = -1
        self.no = -1
        self.no2 = -1
        self.o3 = -1
        self.pm25 = -1
        self.pm10 = -1

