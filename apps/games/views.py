from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.validators import ValidationError
from rest_framework import generics

from games.models import Game, BuyGame
from games.serializers import (
    GameSerializer, 
    GameCreateSerializer,
    BuyGameSerializer
)


class GameViewSet(viewsets.ViewSet):
    """
    ViewSet for Game model.
    """

    queryset = Game.objects.count_game()

    def list(
        self,
        request: Request,
        *args: tuple,
        **kwargs: dict
    ) -> Response:
        serializer: GameSerializer = GameSerializer(
            instance=self.queryset, many=True
        )
        return Response(
            data=serializer.data
        )
    
    def retrieve(
        self, 
        request: Request, 
        pk: int = None
    ) -> Response:
        try:
            game = self.queryset.get(pk=pk)
        except Game.DoesNotExist:
            raise ValidationError('Object not found!', code=404)
        
        serializer = GameSerializer(instance=game)
        return Response(data=serializer.data)

    def create(
        self,
        request: Request,
        *args: tuple,
        **kwargs: dict
    ) -> Response:
        serializer = GameCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        game: Game = serializer.save()
        return Response(
            data={
                "status": "ok",
                "message": f"Game {game.name} is created! Id: {game.pk}"
            }
        )


class BuyGameView(generics.CreateAPIView):
    queryset = BuyGame.objects.all()
    serializer_class = BuyGameSerializer

    def perform_create(self, serializer):
        game = serializer.validated_data['game']
        try:
            if game.count > 0:
                game.count -= 1
                game.save()
                return Response(
                    data={
                        'message': f'Game {game.name} is bought.'
                    }
                )
        except:
            raise ValidationError(f'Game {game.name} is not bought!', code=400)