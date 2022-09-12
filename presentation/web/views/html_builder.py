from presentation.web.views.ihtml_builder import IHtmlBuilder

class HtmlBuilder(IHtmlBuilder):

    def __init__(self):
        self._titre = ""
        self._link = "styles/exempleCss.css"
        self._lang_code = "fr"
        self._encoding = "UTF-8"
        self._html = []
        self.reset()

    @property
    def HTML(self) -> str:
        endbodytag = "</body>"
        endhtmltag = "</html>"

        self._html.append(endbodytag)
        self._html.append(endhtmltag)

        return "".join(self._html)  # convertit les éléments du tableau en une chaine de caractère

    def reset(self):
        self._html.clear()

        doctype = "<!DOCTYPE html>"
        htmltag = f"<html lang=\"{self._lang_code}\">"
        headtag = f"<head><meta charset=\"{self._encoding}\"><title>{self._titre}</title>"
        css_link = f"<link href=\"{self._link}\" rel='stylesheet' type='text/css'>"
        end_head_tag = "</head>"
        bodytag = "<body>"

        self._html.append(doctype)
        self._html.append(htmltag)
        self._html.append(headtag)
        self._html.append(css_link)
        self._html.append(end_head_tag)
        self._html.append(bodytag)

    @property
    def lang_code(self, value):
        self._lang_code = value

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