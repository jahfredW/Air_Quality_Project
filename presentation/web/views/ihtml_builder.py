from abc import ABC, abstractmethod


class IHtmlBuilder(ABC):

    @property
    @abstractmethod
    def HTML(self) -> str:
        pass

    @abstractmethod
    def ajouter_paragraphe(self, texte: str):
        pass

    @abstractmethod
    def ajouter_tableau(self, tableau):
        pass

    @abstractmethod
    def ajouter_html(self, html: str):
        pass
