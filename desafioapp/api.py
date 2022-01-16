from rest_framework import viewsets

from .models import Region
from .models import Fruit
from .serializers import RegionSerializer
from .serializers import FruitSerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class FruitViewSet(viewsets.ModelViewSet):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer