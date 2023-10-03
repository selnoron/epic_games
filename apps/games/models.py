# Django
from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class GameQuerySet(models.QuerySet):

    def count_game(self):
        return self.filter(count__gte=1)


class GameManager(models.Manager):

    def get_queryset(self) -> models.query.QuerySet['Game']:
        return GameQuerySet(
            self.model,
            using=self._db
        )

    def count_game(self):
        return self.get_queryset().count_game()

class Game(models.Model):
    """MY GAME!"""

    name: str = models.CharField(
        verbose_name='игра',
        max_length=200
    )
    price: float = models.DecimalField(
        verbose_name='цена',
        max_digits=11,
        decimal_places=2,
        validators=[
            MinValueValidator(0, message='Мы деньги за игры не даём!')
        ]
    )
    poster: str = models.ImageField(
        verbose_name='постер',
        upload_to='posters'
    )
    rate: float = models.FloatField(
        verbose_name='рейтинг',
        max_length=5
    )
    count: int = models.IntegerField(
        verbose_name='количесво игр',
        default=0
    )

    objects = GameManager()

    class Meta:
        ordering = ('-id',)
        verbose_name = 'игра'
        verbose_name_plural = 'игры'

    def __str__(self) -> str:
        return f'{self.name} | {self.price:.2f}$'


class BuyGame(models.Model):
    user = models.ForeignKey(
        verbose_name='who bought',
        to=User, 
        on_delete=models.CASCADE
    )
    game = models.ForeignKey(
        verbose_name='which game',
        to=Game, 
        on_delete=models.CASCADE
    )
    purchase_date = models.DateTimeField(
        verbose_name='datime_created',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'bought'
        verbose_name_plural = 'buy_history'
    
    def __str__(self) -> str:
        return f'{self.user.username} | {self.game.name}'