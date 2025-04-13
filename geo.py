import requests

def get_coordinates(city_name):
    url = "https://nominatim.openstreetmap.org/search" # OpenStreetMap (via Nominatim)
    params = {"q": city_name, "format": "json"}
    headers = {"User-Agent": "weather-app-example"}  # may work without it
    response = requests.get(url, params=params,headers=headers)
    data = response.json()
    if not data:
        raise Exception("City not found")
    lat = data[0]["lat"]
    lon = data[0]["lon"]
    display_name = data[0]["display_name"]
    return lat, lon, display_name
