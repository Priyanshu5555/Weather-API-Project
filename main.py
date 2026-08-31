import os
import requests
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Get API key from .env
API_KEY = os.getenv("API_KEY")


# OpenWeatherMap API URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


# Function to get weather
def get_weather(city):

    # Data we will send to the API
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    # Send request to the API
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:

        data = response.json()

        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]

        condition = data["weather"][0]["main"]
        description = data["weather"][0]["description"]

        wind_speed = data["wind"]["speed"]

        print("\n==============================")
        print("       WEATHER REPORT")
        print("==============================")

        print(f"City        : {data['name']}")
        print(f"Temperature : {temperature} °C")
        print(f"Feels Like  : {feels_like} °C")
        print(f"Humidity    : {humidity}%")
        print(f"Condition   : {condition}")
        print(f"Description : {description}")
        print(f"Wind Speed  : {wind_speed} m/s")

        print("==============================")

    elif response.status_code == 404:
        print("\n❌ City not found. Please enter a valid city name.")

    elif response.status_code == 401:
        print("\n❌ Invalid API key.")

    else:
        print("\n❌ Something went wrong.")
        print("Status code:", response.status_code)


# Ask user for city
city = input("Enter city name: ")

# Get weather
get_weather(city)