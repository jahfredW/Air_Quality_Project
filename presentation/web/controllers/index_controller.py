from presentation.web.views.index_view import IndexView
from presentation.web.views.index_bulma_view import IndexBulmaView

class IndexController:

    def __init__(self):
        self._view = IndexBulmaView()

    def index(self):
        return self._view.render()
