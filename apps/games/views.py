from abstracts.views import CRUDView
from games.models import Game
from games.forms import CreateForm


class GameView(CRUDView):
    model = Game
    form = CreateForm
    template_create = 'create_game.html'
    template_list = 'list_game.html'
