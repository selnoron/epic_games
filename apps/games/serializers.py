from rest_framework import serializers

from games.models import Game, BuyGame


class GameSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    price = serializers.DecimalField(max_digits=11, decimal_places=2)
    poster = serializers.ImageField()
    rate = serializers.FloatField()
    count = serializers.IntegerField()


class GameCreateSerializer(serializers.ModelSerializer):
    rate = serializers.FloatField(default=0)
    class Meta:
        model = Game
        fields = '__all__'


# Реализовать покупку товара!

class BuyGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyGame
        fields = '__all__'