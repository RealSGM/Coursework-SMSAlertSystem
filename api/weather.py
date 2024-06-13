import requests, os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_WEATHER_KEY')
location = '12.5777,106.9349'
running = True

def get_weather():
    global api_key, location
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()