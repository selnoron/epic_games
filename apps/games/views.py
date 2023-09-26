from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from games.models import Game
from games.serializers import GameSerializer, GameCreateSerializer
from rest_framework.validators import ValidationError



class GameViewSet(viewsets.ViewSet):
    queryset = Game.objects.all()
    def list(
        self,
        request: Request,
        *args: tuple,
        **kwargs: dict,
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
            raise ValidationError('Object Does NOT exists', code=404)
        serializer = GameSerializer(
            instance=game
        )
        return Response(
            data=serializer.data
        )
    
    def create(
        self,
        request: Request,
        *args: tuple,
        **kwargs: dict,
    ) -> Response:
        serializer = GameCreateSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        game: Game = serializer.save()
        return Response(
            data={
                'status': 'ok',
                'message': \
                    f"Game {game.name} is created! ID: {game.pk}"
            }
        )
