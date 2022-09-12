import locale

locale.setlocale(locale.LC_TIME, '')

from datetime import timedelta, date

from presentation.web.views.iview import IView
from presentation.web.views.html_builder import HtmlBuilder
from utils.meteo_common import MeteoCommon


class PollutionVilleView(IView):

    def __init__(self):
        self._nom_ville = ""
        self._prevision_aqi = []
        self._prevision_pm_2_5 = []
        self._prevision_pm_10 = []

    @property
    def nom_ville(self):
        return self._nom_ville

    @nom_ville.setter
    def nom_ville(self, value):
        self._nom_ville = value

    @property
    def prevision_aqi(self):
        return self._prevision_aqi

    @prevision_aqi.setter
    def prevision_aqi(self, value):
        self._prevision_aqi = value

    @property
    def prevision_pm_2_5(self):
        return self._prevision_pm_2_5

    @prevision_pm_2_5.setter
    def prevision_pm_2_5(self, value):
        self._prevision_pm_2_5 = value

    @property
    def prevision_pm_10(self):
        return self._prevision_pm_10

    @prevision_pm_10.setter
    def prevision_pm_10(self, value):
        self._prevision_pm_10 = value

    @property
    def prevision_so2(self):
        return self._prevision_so2

    @prevision_so2.setter
    def prevision_so2(self, value):
        self._prevision_so2 = value

    def _getDay(self):
        htmlPrevisionday = f"<td>Aujourd'hui</td>"
        for index in range(1, len(self.prevision_aqi)):
            htmlPrevisionday += f"<td>{str((date.today() + timedelta(days=index)).strftime('%A %d'))}</td>"

        return htmlPrevisionday


    def _getHTMLPrevisionsLigne(self, prevision_ligne):

        htmlPrevisionLigne = f"<td>{str(prevision_ligne[0])}</td>"

        for index in range(1, len(self.prevision_aqi)):
            htmlPrevisionLigne += f"<td>{str(prevision_ligne[index])}</td>"


        return htmlPrevisionLigne




    def _getHTMLPrevisionsTableau(self):

        htmlPrevisionTableau = "<table border=\"1\">"
        htmlPrevisionTableau += f"<tr><td>jours</td>{self._getDay()}</tr>"
        htmlPrevisionTableau += f"<tr><td>indices</td>{self._getHTMLPrevisionsLigne(self.prevision_aqi)}</tr>"
        htmlPrevisionTableau += f"<tr><td>pm_2_5</td>{self._getHTMLPrevisionsLigne(self.prevision_pm_2_5)}</tr>"
        htmlPrevisionTableau += f"<tr><td>pm_10</td>{self._getHTMLPrevisionsLigne(self.prevision_pm_10)}</tr>"
        htmlPrevisionTableau += f"<tr><td>So2</td>{self._getHTMLPrevisionsLigne(self.prevision_so2)}</tr>"
        htmlPrevisionTableau += "</table>"

        return htmlPrevisionTableau

    def render(self) -> str:
        htmlBuilder = HtmlBuilder()
        htmlBuilder.ajouter_html(f"<h1>Ville : {self.nom_ville}</h1>")
        htmlBuilder.ajouter_paragraphe(
            f"Voici les prévisions pour la ville de {self.nom_ville} obtenues grâce au pattern MVC implémenté sur l'architecture couteau suisse")
        htmlBuilder.ajouter_html(self._getHTMLPrevisionsTableau())
        htmlBuilder.ajouter_paragraphe(f"Le rendu est réalisé côté serveur, par le vue du modèle MVC")

        return htmlBuilder.HTML
