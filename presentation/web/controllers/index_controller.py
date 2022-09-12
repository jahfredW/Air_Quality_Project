from presentation.web.views.index_view import IndexView


class IndexController:

    def __init__(self):
        self._view = IndexBulmaView()

    def index(self):
        return self._view.render()
