# Inside waether_api.py

import requests
base_url = "http://api.weatherapi.com/v1/marine.json"
from config import API_KEY

def get_city_data(location):
    params = {'q': location, 'key': API_KEY}
    try:
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.RequestException as e:
        print(f"Request Exception: {e}")
        return None
