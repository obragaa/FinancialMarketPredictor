import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_percentage_error

def train_and_predict(df, days_ahead=1):
    model = LinearRegression()
    X = df[['close']].values[:-days_ahead]
    y = df['close'].shift(-days_ahead).dropna().values
    model.fit(X, y)
    last_point = np.array([[df['close'].iloc[-1]]])
    future_prediction = model.predict([last_point for _ in range(days_ahead)])
    return {'current_value': df['close'].iloc[-1], 'future_prediction': future_prediction[-1]}