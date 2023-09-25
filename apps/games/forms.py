from django.forms import ModelForm

from games.models import Game


class CreateForm(ModelForm):
    class Meta:
        model = Game
        fields = (
            'name',
            'price',
            'poster',
            'rate'
        )
