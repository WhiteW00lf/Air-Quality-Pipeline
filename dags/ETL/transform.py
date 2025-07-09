import pandas as pd
from datetime import datetime
import os

os.chdir("/home/ubuntu/DE_projects/Air-Quality-Pipeline/data")


def read_csv():
    """
    Reads the weather data from a CSV file and returns a DataFrame.
    """
    try:
        df = pd.read_csv("airquality.csv", parse_dates=["created_at"])
        print("Data read successfully from weather_data.csv")
        df.dropna(inplace=True)

        # Transforming dataframe to a meaningful format
        df["created_at"] = pd.to_datetime(df["created_at"])
        df["co"] = df["co"].astype(float)
        df["no"] = df["no"].astype(float)
        df["no2"] = df["no2"].astype(float)
        df["o3"] = df["o3"].astype(float)
        df["so2"] = df["so2"].astype(float)
        df["pm2_5"] = df["pm2_5"].astype(float)
        df["pm10"] = df["pm10"].astype(float)
        df["nh3"] = df["nh3"].astype(float)
        df["aqi"] = df["aqi"].astype(int)
        return df

    except FileNotFoundError:
        print("File not found. Please ensure the file exists.")
        return pd.DataFrame()  # Return an empty DataFrame if the file does not exist
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return pd.DataFrame()

        # Return an empty DataFrame in case of any other error

        # Drop rows with NaN values
