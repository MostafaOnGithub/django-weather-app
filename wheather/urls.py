from django.urls import path
from .views import CityAPIView

urlpatterns = [
    path('weather', CityAPIView.as_view(), name='city_weather'),
]
