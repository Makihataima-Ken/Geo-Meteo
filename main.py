from geo import get_coordinates
from weather import get_weather

def main():
    city = input("Enter a city name: ")
    try:
        lat, lon, location = get_coordinates(city)
        weather = get_weather(lat, lon)

        print(f"\n📍 Location: {location}")
        print(f"🌡️ Temperature: {weather['temperature']}°C")
        print(f"💨 Wind Speed: {weather['windspeed']} km/h")
        print(f"🕒 Time: {weather['time']}")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
