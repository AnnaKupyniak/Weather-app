import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

def get_lat_long(city, state, country):
    print(API_KEY)
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&limit=1&appid={API_KEY}"
    response = requests.get(url).json()
    if response:
        lat = response[0]['lat']
        lon = response[0]['lon']
        return lat, lon
    return None, None

def get_current_weather(lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()
    weather_data = {
        'main': response['weather'][0]['main'],
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
        'temperature': response['main']['temp']
    }
    return weather_data
