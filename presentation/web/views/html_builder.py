from presentation.web.views.ihtml_builder import IHtmlBuilder

class HtmlBuilder(IHtmlBuilder):

    def __init__(self):
        self._titre = ""
        self._link = "styles/exempleCss.css"
        self._lang_code = "fr"
        self._encoding = "UTF-8"
        self._html = []
        self._custom_head_tags = ""
        self._end_scripts = []
        self.reset()


    @property
    def HTML(self) -> str:

        endbodytag = "</body>"
        endhtmltag = "</html>"
        """
        for script in self._end_scripts:
            self._html.append(script)"""

        self._html.append("<script type='text/javascript' src='./scripts/index.js'></script>")
        self._html.append(endbodytag)
        self._html.append(endhtmltag)

        return "".join(self._html)  # convertit les éléments du tableau en une chaine de caractère

    @property
    def lang_code(self, value):
        self._lang_code = value

    @property
    def custom_head_tags(self, value):
        self._custom_head_tags = value


    def custom_init(self, title, lang_code, encoding, tags ):
        self._titre = title
        self._lang_code = lang_code
        self._encoding = encoding
        self._html = []
        self._custom_head_tags = tags
        self.reset()

    """
    def ajouter_js_avant_body(self, value: str):
        self._end_scripts.append(value)
    """

    def reset(self):
        self._html.clear()

        doctype = "<!DOCTYPE html>"
        htmltag = f"<html lang=\"{self._lang_code}\">"
        headtag = f"<head><meta charset=\"{self._encoding}\"><title>{self._titre}</title>"
        bodytag = "<body>"

        self._html.append(doctype)
        self._html.append(htmltag)
        self._html.append(headtag)
        if self._custom_head_tags != "":
            self._html.append(self._custom_head_tags)
        self._html.append(bodytag)



    def ajouter_paragraphe(self, texte: str):
        self._html.append(f"<p>{texte}</p>")

    def ajouter_zone_texte(self, texte: str):
        self._html.append(f"<textarea cols=\"100\" rows=\"25\" readonly=\"true\">{texte}</textarea>")

    def ajouter_tableau(self, tableau):
        self._html.append("<table>")
        for ligne in tableau:
            self._html.append("<tr>")
            self._html.append(f"<td>{ligne}</td>")
            self._html.append("</tr>")
        self._html.append("</table>")

    def ajouter_html(self, html: str):
        self._html.append(html)