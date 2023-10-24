from celery import shared_task
from django.db.models import F
from games.models import Game


@shared_task
def do_test():
    Game.objects.all().update(
        price=F('price') + 50
    )