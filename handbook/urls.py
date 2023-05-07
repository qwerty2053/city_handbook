from django.urls import path, include

from rest_framework import routers
from .views import EstablishmentListViewSet, EstablishmentViewSet

router = routers.DefaultRouter()
router.register(r'est_list', EstablishmentListViewSet, basename='est_list')
router.register(r'est', EstablishmentViewSet, basename='est')

urlpatterns = [
    path('', include(router.urls))
]
