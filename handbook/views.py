from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from .serializers import EstablishmentListSerializer, EstablishmentSerializer
from .models import Establishment


class EstablishmentListViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentListSerializer


class EstablishmentViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer
