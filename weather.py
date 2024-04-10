from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

# Get data from open weather map API


def get_current_weather(city="Cologne"):
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={
        os.getenv("API_KEY")}&q={city}&units=metric'

    weather_data = requests.get(request_url).json()

    return weather_data

    # Create module
    if __name__ == "__main__":
        print('\n*** Get Current Weather Conditions***\n')

        # Check for empty Strings or strings with only spaces
        if not bool(city.strip()):
            city = "Cologne"

        city = input("\nPlease enter a city name: ")

        weather_data = get_current_weather(city)

        print("\n")
        pprint(weather_data)
