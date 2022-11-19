from rest_framework import viewsets

from api import serializer, models


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = models.Pokemon.objects.all()
    serializer_class = serializer.PokemonSerializer
    ordering_fields = '__all__'


class TreinadorViewSet(viewsets.ModelViewSet):
    queryset = models.Treinador.objects.all()
    serializer_class = serializer.TreinadorSerializer
    ordering_fields = "__all__"

