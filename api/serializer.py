from rest_framework import serializers

from api import models


class GetIdFromQuerySet(serializers.HyperlinkedModelSerializer):
    def get_field_names(self, declared_fields, info):
        _fields = super().get_field_names(declared_fields, info)
        _fields.insert(0, 'id')
        return _fields


class PokemonSerializer(GetIdFromQuerySet):
    class Meta:
        model = models.Pokemon
        fields = '__all__'


class TreinadorSerializer(GetIdFromQuerySet):
    class Meta:
        model = models.Treinador
        fields = '__all__'
        
class RegiaoSerializer(GetIdFromQuerySet):
    class Meta:
        model = models.Regiao
        fields = '__all__'



class PoolSerializer(GetIdFromQuerySet):
    class Meta:
        model = models.Pool
        fields = "__all__"


class PokebolaSerializer(GetIdFromQuerySet):
    class Meta:
        model = models.Pokebola
        fields = '__all__'