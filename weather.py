from datetime import datetime, timedelta

import requests, json

cities = ['London', 'Vancouver', 'Toronto', 'Tokyo', 'Chicago']
url = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}"
weather_key = "185dac1d7c90cd6aba0849cae0e0fcc3"
weather_short = ["", "", "", "", ""]
last_weather_update = None

##Weather updater
# get_weather() this function retrieves weather from the openweathermap api at intervals of 1 hour 
def get_weather():
    global last_weather_update, cities, url, weather_key, weather_short
    if last_weather_update is None or last_weather_update + timedelta(hours = 1) > datetime.now():
        last_weather_update = datetime.now()
        updated_weather = []
        for i in cities:
            req = requests.get(url.format(city=i, weather_key=weather_key)).json()['weather'][0]['description']
            updated_weather.append(req)
        weather_short = updated_weather
    return weather_short

# get_cities() this function returns list of supported cities
def get_cities():
    return cities
            