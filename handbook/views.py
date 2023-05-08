from django.db.models import QuerySet
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, generics

from .serializers import EstablishmentListSerializer, EstablishmentSerializer, CityWithIdSerializer, \
                        CategoryWithIdSerializer

from .models import Establishment, City, Category


class EstablishmentListViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentListSerializer


class CityListViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = City.objects.all()
    serializer_class = CityWithIdSerializer


class CategoryListViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryWithIdSerializer


class EstablishmentViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer


class EstablishmentCityListAPIView(generics.ListAPIView):
    serializer_class = EstablishmentListSerializer

    def get_queryset(self):
        city = self.kwargs['city_id']
        return Establishment.objects.filter(city=city)


class EstablishmentCategoryListAPIView(generics.ListAPIView):
    serializer_class = EstablishmentListSerializer

    def get_queryset(self):
        category = self.kwargs['category_id']
        return Establishment.objects.filter(category=category)


class EstablishmentAddressSearchAPIView(generics.ListAPIView):
    serializer_class = EstablishmentSerializer

    def get_queryset(self):
        # Empty search will return all the objects
        # so we'll use str.strip and check if query is not empty
        address = self.kwargs['address'].strip()
        if not address:
            return Establishment.objects.none()
        return Establishment.objects.filter(address__icontains=address)


class EstablishmentTitleSearchAPIView(generics.ListAPIView):
    serializer_class = EstablishmentSerializer

    def get_queryset(self):
        # Empty search will return all the objects
        # so we'll use str.strip and check if query is not empty
        title = self.kwargs['title']
        if not title:
            return Establishment.objects.none()
        return Establishment.objects.filter(title__icontains=title)
