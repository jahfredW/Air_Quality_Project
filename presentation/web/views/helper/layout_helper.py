from utils.configuration import Configuration


class LayoutHelper:

    @staticmethod
    def get_hero_head() -> str:
        items = []
        items.append("<div class=\"hero-head\">")
        items.append("<nav class=\"navbar has-background-link\" role=\"navigation\" aria-label=\"main navigation\">")
        items.append("<div class=\"navbar-brand\">")
        items.append("<a class=\"navbar-item\" href=\"http://127.0.0.1:8050/\">")
        items.append("<span class=\"is-uppercase has-text-weight-bold has-text-white\">On va courir ? </span>")
        items.append("</a>")
        items.append("<a role=\"button\" class=\"navbar-burger has-text-white\" aria-label=\"menu\" aria-expanded=\"false\"")
        items.append("data-target=\"navbarMenu\">")
        items.append("<span aria-hidden=\"true\"></span>")
        items.append("<span aria-hidden=\"true\"></span>")
        items.append("<span aria-hidden=\"true\"></span>")
        items.append("</a>")
        items.append("</div>")
        items.append("<div id=\"navbarMenu\" class=\"navbar-menu\">")
        items.append("<div class=\"navbar-start\">")
        items.append("<a class=\"navbar-item has-text-white\">")
        items.append("Accueil")
        items.append("</a>")
        items.append("<div class=\"navbar-item has-dropdown is-hoverable\">")
        items.append("<a class=\"navbar-link has-text-white\">")
        items.append("Plus...")
        items.append("</a>")
        items.append("<div class=\"navbar-dropdown\">")
        items.append("<a class=\"navbar-item\">")
        items.append("Configuration")
        items.append("</a>")
        items.append("<a class=\"navbar-item\">")
        items.append("A propos")
        items.append("</a>")
        items.append("<a class=\"navbar-item\">")
        items.append("Qui sommes nous")
        items.append("</a>")
        items.append("</div>")
        items.append("</div>")
        items.append("</div>")
        items.append("</div>")
        items.append("<div id=\"navbarMenu\" class=\"navbar-menu is-active\">")
        items.append("<div class=\"navbar-end\">")
        items.append("<div class=\"navbar-item\">")
        items.append("<form action=\"http://127.0.0.1:8050/pollution/villes\" method=\"post\">")
        items.append("<div class=\"block pr-6\">")
        items.append("<div class=\"columns is-mobile is-gapless\">")
        items.append("<div class=\"column is-full\">")
        items.append("<div class=\"control\">")
        items.append("<input name=\"ville\" class=\"input\" type=\"text\" placeholder=\"Ville...\">")
        items.append("</div>")
        items.append("</div>")
        items.append("<div class=\"column\">")
        items.append("<div class=\"control\">")
        items.append("<button class=\"button is-primary\">")
        items.append("<span class=\"icon\">")
        items.append("<i class=\"fas fa-search\"></i>")
        items.append("</span>")
        items.append("</button>")
        items.append("</div>")
        items.append("</div>")
        items.append("</div>")
        items.append("</div>")
        items.append("</form>")
        items.append("</div>")
        items.append("</div>")
        items.append("</div>")
        items.append("</nav>")
        items.append("</div>")

        return "".join(items)

    @staticmethod
    def get_header_tags() -> str:
        header_tags = f"<link rel=\"stylesheet\" href=\"{Configuration().get_instance().web_url_css_directory}\styles.css\">"
        header_tags += "<link rel=\"stylesheet\" href=\"https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css\">"
        header_tags += "<script defer src=\"https://use.fontawesome.com/releases/v6.1.1/js/all.js\"></script>"

        return header_tags

    @staticmethod
    def get_hero_start() -> str:
        return "<section class =\"hero is-fullheight background_hero\">"

    @staticmethod
    def get_hero_end() -> str:
        return "</section>"

    @staticmethod
    def get_hero_footer() -> str:

        items = []
        items.append("<div class=\"hero-foot\">")
        items.append("<div class=\"container has-text-right\">")
        items.append("<p class=\"footer-text has-text-white\">")
        items.append("<strong>Fred G. ingeniering</strong>")
        items.append("</p>")
        items.append("</div>")
        items.append("</div>")

        return "".join(items)
