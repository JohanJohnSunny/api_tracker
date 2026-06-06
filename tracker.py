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
    print(f"Server response code {response.status_code}")
    try:
        if response.status_code == 200:
            data = response.json()
            print("\n DATA RECEIVED FROM SERVER \n")
            print("-"*50,end='\n')
            for key,value in data.items():
                print(f" {key.ljust(12)} :{value}")
            print("-"*50,end='\n')
        elif response.status_code == 404:
            print(f" Error: The city '{city_name}' was not found. Please check your spelling!")
        elif response.status_code == 401:
            print("Error: Unauthorized access. Please verify your WEATHER_API_KEY in the .env file.")
        else:
            print(f"Error: Server returned an unexpected status code: {response.status_code}")
    except requests.exceptions.Timeout:
        print("Error: The connection timed out. Please check your network speed.")
    except requests.exceptions.RequestException as e:
        print(f"Error: A network error occurred: {e}")

if __name__ == "__main__":
    if not API_KEY:
        print("Error: WEATHER_API_KEY missing from .env file!")
    else:
        # Test it with a major city!
        get_weather(input("Enter a city:"))
