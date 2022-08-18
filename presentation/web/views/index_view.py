from presentation.web.views.html_builder import HtmlBuilder
from presentation.web.views.iview import IView


class IndexView(IView):
    def render(self) -> str:
        htmlBuilder = HtmlBuilder()
        htmlBuilder.ajouter_html("<h1>Bienvenue dans l'application météo !</h1>")
        htmlBuilder.ajouter_paragraphe("Pourquoi vous êtes là ? Car vous vous êtes connecté sur le serveur de l'application météo sans fournir d'url spécifique.")
        htmlBuilder.ajouter_paragraphe("Tout va bien, ce n'est pas grave :-) voici la liste des urls qui sont accessibles pour utiliser l'application météo :")
        htmlBuilder.ajouter_html("<br>")
        htmlBuilder.ajouter_html("<h2>/villes/{ville}</h2>")
        htmlBuilder.ajouter_paragraphe("Permet de soumettre le nom d'une ville via un formulaire HTML et obtenir en retour une page web contenant les prévisions météo pour la ville.")

        return htmlBuilder.HTML
