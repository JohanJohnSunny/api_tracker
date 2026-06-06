import os
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
    





if __name__ == "__main__":
    check_setup()