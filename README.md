# Geo-Meteo

A simple Python command-line application that fetches real-time weather data for any city using:  
- **OpenStreetMap (Nominatim API)** for geocoding  
- **Open-Meteo API** for weather data  

## 🚀 Features
- Get **latitude** and **longitude** from a city name  
- Retrieve **current temperature**, **wind speed**, and **time**  
- Uses free, public APIs with no authentication required  
- Minimal dependencies (only `requests`)  

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/weather-app.git
cd Geo-Meteo
```

2. **Inatll dependencies**
```bash
pip install requests
```

## ▶️ Usage
Run the app in your terminal:
```bash
python main.py
```

## 📂 Project Structure
```bash
weather-app/
│── main.py          # Main program logic
│── geo.py           # Geocoding function (get_coordinates)
│── weather.py       # Weather retrieval function (get_weather)
└── README.md        # Documentation
```

## APIs Used
[OpenStreetMap]: https://nominatim.openstreetmap.org/
[Open-Meteo]: https://open-meteo.com/

This project uses [OpenStreetMap] for geocoding and [Open-Meteo] for weather data.



