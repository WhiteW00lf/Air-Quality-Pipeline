import pandas as pd
from datetime import datetime
def read_csv():
    """
    Reads the weather data from a CSV file and returns a DataFrame.
    """
    try:
        df = pd.read_csv(f"../data/{datetime.today().date()}_weather_data.csv",header=None,names=["created_at", "temp", "humidity", "description", "clouds", "wind_speed", "pressure"])
        print("Data read successfully from weather_data.csv")
        df.dropna(inplace=True)
        
        #Transforming dataframe to a meaningful format
        df['created_at'] = pd.to_datetime(df['created_at'])
        df['temp'] = df['temp'].astype(int)
        df['humidity'] = df['humidity'].astype(float)
        df['clouds'] = df['clouds'].astype(float)
        df['wind_speed'] = df['wind_speed'].astype(float)
        df['pressure'] = df['pressure'].astype(float)
        return df
        print(df.dtypes)
    except FileNotFoundError:
        print("File not found. Please ensure the file exists.")
        return pd.DataFrame()  # Return an empty DataFrame if the file does not exist
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return pd.DataFrame() 
        
         # Return an empty DataFrame in case of any other error
       
          # Drop rows with NaN values

read_csv()
   