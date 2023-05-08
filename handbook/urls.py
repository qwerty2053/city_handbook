from django.urls import path, include
from rest_framework import routers
from .views import EstablishmentListViewSet, EstablishmentViewSet, EstablishmentCityListAPIView, \
                   EstablishmentCategoryListAPIView, CategoryListViewSet, CityListViewSet, \
                   EstablishmentAddressSearchAPIView, EstablishmentTitleSearchAPIView

router = routers.DefaultRouter()
router.register(r'category_list', CategoryListViewSet, basename='category_list')
router.register(r'city_list', CityListViewSet, basename='city_list')
router.register(r'est_list', EstablishmentListViewSet, basename='est_list')
router.register(r'est', EstablishmentViewSet, basename='est')


urlpatterns = [
    path('', include(router.urls)),
    path('city/<int:city_id>', EstablishmentCityListAPIView.as_view()),
    path('category/<int:category_id>', EstablishmentCategoryListAPIView.as_view()),
    path('search/address/<str:address>', EstablishmentAddressSearchAPIView.as_view()),
    path('search/title/<str:title>', EstablishmentTitleSearchAPIView.as_view()),
]
