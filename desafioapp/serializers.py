from rest_framework import serializers
from .models import Region
from .models import Fruit

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('__all__')

class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields = ('__all__')