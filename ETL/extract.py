from dotenv import load_dotenv
from datetime import datetime
import pandas as pd
import os
import requests

today_day = datetime.today().date()


def extract_data():
    """
    Extracts data from the OpenWeather API and returns a DataFrame.
    """
    # Load environment variables
    load_dotenv()
    mykey = os.getenv("myapikey")
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat=19.0785451&lon=72.878176&appid={mykey}"
    # print(url)
    try:
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            # Extract relevant data from the JSON response
            for item in data["list"]:
                created_at = datetime.fromtimestamp(item["dt"]).strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
                aqi = item["main"]["aqi"]
                co = item["components"]["co"]
                no = item["components"]["no"]
                no2 = item["components"]["no2"]
                o3 = item["components"]["o3"]
                so2 = item["components"]["so2"]
                pm2_5 = item["components"]["pm2_5"]
                pm10 = item["components"]["pm10"]
                nh3 = item["components"]["nh3"]

                # Create a DataFrame for each day's data
                air_quality_df = pd.DataFrame(
                    {
                        "created_at": [created_at],
                        "aqi": [aqi],
                        "co": [co],
                        "no": [no],
                        "no2": [no2],
                        "o3": [o3],
                        "so2": [so2],
                        "pm2_5": [pm2_5],
                        "pm10": [pm10],
                        "nh3": [nh3],
                    }
                )

                # Save the DataFrame to a CSV file
                file_name = "airquality.csv"
                if not os.path.exists(f"../data/{file_name}"):
                    air_quality_df.to_csv(f"../data/{file_name}", index=False)
                else:
                    air_quality_df.to_csv(
                        f"../data/{file_name}", mode="a", header=False, index=False
                    )
                print(f"Data extracted and saved to {file_name}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")




# Mumbai
# lat = 19.0785451
# lon= 72.878176
