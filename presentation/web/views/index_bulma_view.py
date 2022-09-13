from presentation.web.views.helper.layout_helper import LayoutHelper
from presentation.web.views.html_builder import HtmlBuilder
from presentation.web.views.iview import IView

class IndexBulmaView(IView):
    def render(self) -> str:
        htmlBuilder = HtmlBuilder()

        htmlBuilder.custom_init("On va courir?", "fr", "UTF-8", LayoutHelper.get_header_tags())
        htmlBuilder.ajouter_html(LayoutHelper.get_hero_start())
        htmlBuilder.ajouter_html(LayoutHelper.get_hero_head())

        htmlBuilder.ajouter_html("<div class =\"hero-body\">")
        htmlBuilder.ajouter_html("<div class=\"container has-text-centered has-text-black\">")
        htmlBuilder.ajouter_html("<p class=\"title has-text-black\">Et si on allait courir ?</p>")
        htmlBuilder.ajouter_html("<p class=\"subtitle has-text-black\">Recherchez votre ville pour connaitre les données pollution</p>")
        htmlBuilder.ajouter_html("</div>")
        htmlBuilder.ajouter_html("</div>")

        htmlBuilder.ajouter_html("</nav>")

        htmlBuilder.ajouter_html(LayoutHelper.get_hero_footer())
        htmlBuilder.ajouter_html(LayoutHelper.get_hero_end())
        return htmlBuilder.HTML
