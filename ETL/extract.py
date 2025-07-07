from dotenv import load_dotenv
import pandas as pd
import os
import requests


def extract_data():
    """
    Extracts data from the OpenWeather API and returns a DataFrame.
    """
    # Load environment variables
    load_dotenv()
    mykey = os.getenv("myapikey")
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat=19.0785451&lon=72.878176&appid={mykey}&exclude=minutely,hourly,alerts&units=metric"
    print(url)
    try:
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            print(data)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")


extract_data()

# Mumbai
# lat = 19.0785451
# lon= 72.878176
