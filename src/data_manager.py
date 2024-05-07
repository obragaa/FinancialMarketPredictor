# src/data_manager.py
import requests
import pandas as pd
from src.config import API_KEY, BASE_URL

def process_financial_data(data, interval):
    """Process financial time series data into a pandas DataFrame."""
    try:
        time_series = data['Time Series (' + interval + ')']
        df = pd.DataFrame.from_dict(time_series, orient='index', dtype=float)
        df.columns = ['open', 'high', 'low', 'close', 'volume']
        return df
    except KeyError:
        raise ValueError("Data processing error: Check the API response structure or the interval key.")

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
    return data, interval

def get_latest_data(df):
    """Extract the latest data point to use for prediction."""
    latest_data = df.iloc[-1]  # Pega o último registro
    return latest_data.to_dict()
