from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from games.models import Game
from games.serializers import GameSerializer
from rest_framework.validators import ValidationError
from rest_framework.decorators import api_view


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
    
    def post(request):
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(
            data=serializer.data
        )
