import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")

city = input("enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url)

    response.raise_for_status()

    data = response.json()

    city_name = data["name"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather =  data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]


    print("\n=========== weather information=========")
    print(f"city: {city}")
    print(f"Temperature: {temperature} degree celcius")
    print(f"humidity {humidity}")
    print(f"weather: {weather}")
    print(f"wind speed: {wind_speed}")

except requests.exceptions.HTTPError:
    print("city not found or invalid request")

except requests.exceptions.ConnectionError:
    print("Error: no internet connection")
except requests.exceptions.Timeout:
    print("Error: request timed out")

except requests.exceptions.RequestException as e:
    print(f"an error as occurred: {e}")