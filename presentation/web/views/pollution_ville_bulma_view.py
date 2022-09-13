import datetime

from presentation.web.views.helper.layout_helper import LayoutHelper
#from presentation.web.views.helper.ui_helper import UIHelper
from presentation.web.views.html_builder import HtmlBuilder
from presentation.web.views.iview import IView
from utils.meteo_common import MeteoCommon


class PollutionVilleBulmaView(IView):

    def __init__(self):
        self._nom_ville = ""
        self._aqi_jour = {}
        self._pm10_jour = {}
        self._pm25_jour = {}
        self._so2_jour = {}
        self._previsions_description = ""

    @property
    def nom_ville(self):
        return self._nom_ville

    @nom_ville.setter
    def nom_ville(self, value):
        self._nom_ville = value

    @property
    def aqi_jour(self):
        return self._aqi_jour

    @aqi_jour.setter
    def aqi_jour(self, value):
        self._aqi_jour = value

    @property
    def pm10_jour(self):
        return self._pm10_jour

    @pm10_jour.setter
    def pm10_jour(self, value):
        self._pm10_jour = value

    @property
    def pm25_jour(self):
        return self._pm25_jour

    @pm25_jour.setter
    def pm25_jour(self, value):
        self._pm25_jour = value

    @property
    def so2_jour(self):
        return self._so2_jour

    @so2_jour.setter
    def so2_jour(self, value):
        self._so2_jour = value

    @property
    def previsions_description(self):
        return self._previsions_description

    @previsions_description.setter
    def previsions_description(self, value):
        self._previsions_description = value


    def build_article(self, so2, pm25, pm10, aqi, description):

        html_article = "<div class=\"tile is-ancestor mt-5\">"
        html_article += "<div class=\"tile is-vertical is-4\">"
        html_article += "<div class=\"tile >"
        html_article += "<div class=\"tile is-parent \">"
        html_article += "<article class=\"tile is-child box \" style=\"background: linear-gradient(to bottom, #72EDF2AA 30%, #5151E5BC 90%)\">"
        html_article += self._getHTMLPrevisionArticleAqi(aqi, description)
        html_article += self._getHTMLPrevisionArticle("pm10", pm10)
        html_article += self._getHTMLPrevisionArticle("pm25", pm25)
        html_article += self._getHTMLPrevisionArticle("souffre", so2)


        html_article += "</article>"
        html_article += "</div>"
        html_article += "</div>"

        return html_article



    def _getHTMLPrevisionArticleAqi(self, aqi, description):


        html_article = "<div class=\"level-item has-text-centered\">"
        html_article += "<div>"
        html_article += "<p class=\"heading\">"
        html_article += "Indice :"
        html_article += "</p>"
        html_article += "<p class= \"title\">"
        html_article += f"{aqi}"
        html_article += "<p>"
        html_article += "<div class=\"subtitle mt-2\">"
        html_article += f"{description}"
        html_article += "</div>"
        html_article += "</div>"
        html_article += "</div>"

        return html_article



    def _getHTMLPrevisionArticle(self, nom,  polluant):

        html_article = "<div class=\"level-item has-text-centered mt-6\">"
        html_article += "<div>"
        html_article += "<p class=\"heading\">"
        html_article += f"{nom} :"
        html_article += "</p>"
        html_article += "<p class= \"title\">"
        html_article += f"{polluant} micro_g /m3"
        html_article += "<p>"


        return html_article


    def render(self) -> str:

        jour = datetime.date.today()
        aqi = self.aqi_jour[0]
        pm10 = self.pm10_jour[0]
        pm25 = self.pm25_jour[0]
        so2 = self.so2_jour[0]
        description = self.previsions_description
        htmlBuilder = HtmlBuilder()

        htmlBuilder.custom_init("Application météo", "fr", "UTF-8", LayoutHelper.get_header_tags())
        htmlBuilder.ajouter_html(LayoutHelper.get_hero_start())
        htmlBuilder.ajouter_html(LayoutHelper.get_hero_head())

        # mettre ici le contenu de la page
        htmlBuilder.ajouter_html("<div class =\"hero-body\">")
        htmlBuilder.ajouter_html("<div class =\"container\">")
        htmlBuilder.ajouter_html("<div class=\"container has-text-centered mb-7\">")
        htmlBuilder.ajouter_html(f"<p class=\"title has-text-white\">Pollution de la ville de {self.nom_ville} ce jour</p>")
        htmlBuilder.ajouter_html("</div>")
        htmlBuilder.ajouter_html("<div class=\"container mt-4\">")
        htmlBuilder.ajouter_html(self.build_article(so2, pm25, pm10, aqi, description))
        htmlBuilder.ajouter_html("</div>")
        htmlBuilder.ajouter_html("</div>")
        htmlBuilder.ajouter_html("</div>")
        htmlBuilder.ajouter_html("</div>")
        htmlBuilder.ajouter_html("</div>")
        htmlBuilder.ajouter_html(LayoutHelper.get_hero_footer())
        htmlBuilder.ajouter_html(LayoutHelper.get_hero_end())
        return htmlBuilder.HTML
