from django.urls import path, include
from . import views
from .views import CombinedDataViewSet
# from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'advice', views.CombinedDataViewSet, basename='advice')

urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework', namespace='rest_framework'))
]