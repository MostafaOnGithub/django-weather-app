from rest_framework.response import Response
import requests
from rest_framework.views import APIView
from geopy.geocoders import Nominatim

class CityAPIView(APIView):  
    def get(self, request, format=None):
        API_key = 'Your Api Key'
        city = request.query_params.get("city") 
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_key}'  # Correct the URL and parameter spelling
        data = requests.get(url).json()  
        weather_data = {
            "city":city,
            "temperature":data['main']['temp'],
            "feels_like":data["main"]["feels_like"],
            "description":data["weather"][0]["description"],
        }
        return Response(weather_data)
    
