# I created a get_weather_info function for fetching weather information
# and a display_forecast function for displaying the forecast

import json
import requests
#from IPython.display import Image, display
from pgeocode import Nominatim

DEGREE_SIGN = u"\N{DEGREE SIGN}"  # Define DEGREE_SIGN

def get_weather_info(zip_code):
    """
    Fetches weather information for the provided zip code.

    Params:
        zip_code (str): A valid US zip code, like "20057" or "06510".

    Returns:
        dict: Weather information as a dictionary.
    """
    nomi = Nominatim('US')
    geo = nomi.query_postal_code(zip_code)
    latitude, longitude = geo["latitude"], geo["longitude"]

    request_url = f"https://api.weather.gov/points/{latitude},{longitude}"
    response = requests.get(request_url)
    response.raise_for_status()  # Check for API request errors
    parsed_response = json.loads(response.text)

    forecast_url = parsed_response["properties"]["forecast"]
    forecast_response = requests.get(forecast_url)
    forecast_response.raise_for_status()  # Check for API request errors
    parsed_forecast_response = json.loads(forecast_response.text)

    return parsed_forecast_response["properties"]["periods"]

def display_forecast(periods):
    """
    Displays the weather forecast for the provided periods.

    Params:
        periods (list): List of weather periods to display.
    """
    for period in periods:
        print("-------------")
        print(period["name"], period["startTime"][0:7])
        print(period["shortForecast"], f"{period['temperature']} {DEGREE_SIGN}{period['temperatureUnit']}")
        #display(Image(url=period["icon"]))

def main():
    print("-----------")
    print("EXAMPLE IMAGES:")
    print("-----------")

    # Example images
    #display(Image(url="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Georgetown_Hoyas_logo.svg/64px-Georgetown_Hoyas_logo.svg.png"))
    #display(Image(url="https://www.python.org/static/community_logos/python-powered-w-200x80.png"))
    #display(Image(url="https://api.weather.gov/icons/land/day/sct?size=medium"))

    zip_code = input("Please input a zip code (e.g. '06510'): ") or "06510"
    print("ZIP CODE:", zip_code)

    # Fetch and display weather information
    periods = get_weather_info(zip_code)
    display_forecast(periods)

if __name__ == "__main__":
    main()
