# City Data Reporter

## About the Project

City Data Reporter is a Python program that lets the user enter a city name and get the current weather for that city.

The program uses the OpenWeather API to get live weather data. It displayts the city, country, temperature, humidity, and weather description.

The program also saves information to a CSV file called "city_data.csv". It can then read the CSV file and display how many cities are saved along with their temperatures.

## Features

- Asks the user to enter a city name
- Checks to see if the city name is empty
- Gets live weather data from OpenWeather
- Displays the city, country, weather, humidity, and weather description
- Reads data from the CSV file
- Displays the amount of cities saved and their temperatures
- Handles invalid city names and invalid API keys

## Requirements

You need Python installed on your computer.

You will also need the 'requests' library.

Intall it by running:

```bash
python -m pip install requests
```


## OpenWeather API Key

This program requires a free OpenWeather API Key.

1. Go to https://openweathermap.org/
2. Create a free account or sign in
3. Go to API Keys in section.
4. Copy your API key.
5. Run the program and enter the API key when asked.

## How to Run

Open a terminal in th efolder that contains 'reporter.py'.

Run:
```bash
python reporter.py
```


The program will ask you for your OpenWeather API key and then ask you to enter a city name.

Example:

```text
Enter your OpenWeather API Key:
Enter a city name: Saint Paul
```


The program will display the current weather and save th einformation to 'city_data.csv'


## Files

- 'reporter.py' - Main Python proram
- city_data.csv' - Stores saved weather data
- 'README.md' - Project information and instructions

## Libraries Used

- 'requests' - Gets weather data from the API
- 'json' - Reads the JSON data returned by the API
- 'csv' - Reads and writes the CSV file

## Youtube Link

