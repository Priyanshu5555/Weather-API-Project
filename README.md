# Weather API Project

This is a simple Python project that uses the OpenWeatherMap API to get the current weather of a city.

The user enters a city name, and the program displays the weather details like temperature, humidity, weather condition and wind speed.

## What it shows

* City name
* Temperature
* Feels like temperature
* Humidity
* Weather condition
* Weather description
* Wind speed

## Technologies Used

* Python
* Requests
* python-dotenv
* OpenWeatherMap API

## Project Structure

```text
Weather-API-Project/
│
├── .env
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

## Setup

First, install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project folder and add your API key:

```env
API_KEY=your_api_key_here
```

The API key is kept in `.env` instead of writing it directly in the Python code.

## Run the Project

Run:

```bash
python main.py
```

Then enter the city name:

```text
Enter city name: Agra
```

The program will fetch the weather and display the result.

## Example

```text
==============================
       WEATHER REPORT
==============================
City        : Agra
Temperature : 30 °C
Feels Like  : 33 °C
Humidity    : 60%
Condition   : Clouds
Description : scattered clouds
Wind Speed  : 3.5 m/s
==============================
```

## What I Learned

While making this project, I learned how to:

* Work with APIs in Python
* Send requests using the `requests` library
* Read JSON data
* Use environment variables
* Keep an API key in a `.env` file
* Handle basic API errors
* Use Git and GitHub

## Future Changes

I may add more features later, such as a weather forecast and more weather details.
