import requests

def get_weather(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast" # Open-Meteo API
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": "true"
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data["current_weather"]
