import csv
import json
from pathlib import Path

import requests


API_URL = "https://api.openweathermap.org/data/2.5/weather"
CSV_FILE = Path(__file__).with_name("city_data.csv")


def get_city_name():
    """Ask the user for a city name and make sure it is not empty."""
    while True:
        city_name = input("Enter a city name: ").strip()

        if city_name:
            return city_name

        print("City name cannot be empty. Please try again.")


def get_weather_data(city_name, api_key):
    """Get current weather information from the OpenWeather API."""
    parameters = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(API_URL, params=parameters)

    if response.status_code == 404:
        print("City not found.")
        return None

    if response.status_code == 401:
        print("Invalid API key.")
        return None

    data = json.loads(response.text)

    return data


def process_weather_data(data):
    """Extract the needed weather information from the API data."""
    weather_data = {
        "City": data["name"],
        "Country": data["sys"]["country"],
        "Temperature (C)": data["main"]["temp"],
        "Humidity (%)": data["main"]["humidity"],
        "Description": data["weather"][0]["description"]
    }

    return weather_data


def display_weather(weather_data):
    """Displays the weather information in the terminal."""
    print("\nCurrent Weather")
    print("----------------")
    print(f"City: {weather_data['City']}")
    print(f"Country: {weather_data['Country']}")
    print(f"Temperature: {weather_data['Temperature (C)']}°C")
    print(f"Humidity: {weather_data['Humidity (%)']}%")
    print(f"Description: {weather_data['Description']}")


def save_to_csv(weather_data):
    """Save the weather information to city_data.csv."""
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:
        field_names = [
            "City",
            "Country",
            "Temperature (C)",
            "Humidity (%)",
            "Description"
        ]

        writer = csv.DictWriter(file, fieldnames=field_names)

        if file.tell() == 0:
            writer.writeheader()

        writer.writerow(weather_data)

    print("Weather data saved to city_data.csv")


def read_csv_report():
    """Read the CSV file and display saved cities and temperatures."""
    with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        cities = list(reader)

    print(f"\nNumber of cities in the file: {len(cities)}")

    for city in cities:
        print(f"{city['City']}: {city['Temperature (C)']}°C")


def main():
    """Run the City Data Reporter program."""
    api_key = input("Enter your OpenWeather API Key: ").strip()
    city_name = get_city_name()

    data = get_weather_data(city_name, api_key)

    if data is not None:
        weather_data = process_weather_data(data)
        display_weather(weather_data)
        save_to_csv(weather_data)
        read_csv_report()


if __name__ == "__main__":
    main()