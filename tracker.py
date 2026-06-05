import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

def check_setup():
    if not API_KEY:
        print("Error: Could not find WEATHER_API_KEY. Check your .env file!")
        return
    print(f"Success! Found API Key starting with: {API_KEY[:5]}...")

if __name__ == "__main__":
    check_setup()