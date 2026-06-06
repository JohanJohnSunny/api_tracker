import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city_name):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    query_parameters = {
        "q" : city_name,
        "appid":API_KEY,
        "units":"metric"
    }

    print(f"Sending request to the server for city {city_name}")

    response = requests.get(url = BASE_URL,params = query_parameters)




if __name__ == "__main__":
    check_setup()