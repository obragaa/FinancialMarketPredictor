# src/data_manager.py
import requests
import pandas as pd
from src.config import API_KEY, BASE_URL

def fetch_financial_data(symbol, interval='5min', function='TIME_SERIES_INTRADAY'):
    """Fetch financial data from Alpha Vantage API."""
    params = {
        'function': function,
        'symbol': symbol,
        'interval': interval,
        'apikey': API_KEY,
        'datatype': 'json'
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data, interval  # Retornar também o interval

def process_financial_data(data, interval):
    """Process financial time series data into a pandas DataFrame."""
    time_series_key = 'Time Series (' + interval + ')'
    time_series = data[time_series_key]
    df = pd.DataFrame.from_dict(time_series, orient='index')
    df.columns = [col.split()[-1] for col in df.columns]  # Simplifica os nomes das colunas
    df = df.astype(float)
    df.index = pd.to_datetime(df.index)
    return df


def get_latest_data(df):
    """Extract the latest data point to use for prediction."""
    latest_data = df.iloc[-1]  # Pega o último registro
    return latest_data.to_dict()

def save_data_to_csv(df, filename='financial_data.csv'):
    """Save DataFrame to a CSV file."""
    df.to_csv(filename, mode='a', header=not pd.os.path.exists(filename))  # Append if file exists
