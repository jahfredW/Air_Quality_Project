import datetime
from business.entities.ville import Ville


class Pollution_instant:
    def __init__(self):
        self.aqi: int = 0
        self.co: float = 0
        self.no: float = 0
        self.no2: float = 0
        self.o3: float = 0
        self.so2: float = 0
        self.pm2_5: float = 0
        self.pm10: float = 0
        self.nh3: float = 0
        self.instant = None
        self.ville = Ville()

    @property
    def aqi(self):
        return self._aqi

    @aqi.setter
    def aqi(self, value):
        self._aqi = value

    @property
    def co(self):
        return self._co

    @co.setter
    def co(self, value):
        self._co = value

    @property
    def no(self):
        return self._no

    @no.setter
    def no(self, value):
        self._no = value

    @property
    def no2(self):
        return self._no2

    @no2.setter
    def no2(self, value):
        self._no2 = value

    @property
    def o3(self):
        return self._o3

    @o3.setter
    def o3(self, value):
        self._o3 = value

    @property
    def so2(self):
        return self._so2

    @so2.setter
    def so2(self, value):
        self._so2 = value

    @property
    def pm2_5(self):
        return self._pm2_5

    @pm2_5.setter
    def pm2_5(self, value):
        self._pm2_5 = value

    @property
    def pm10(self):
        return self._pm10

    @pm10.setter
    def pm10(self, value):
        self._pm10 = value

    @property
    def nh3(self):
        return self._nh3

    @nh3.setter
    def nh3(self, value):
        self._nh3 = value

    @property
    def instant(self):
        return self._instant

    @instant.setter
    def instant(self, value):
        self._instant = value

    @property
    def ville(self):
        return self._ville

    @ville.setter
    def ville(self, value):
        self._ville = value



