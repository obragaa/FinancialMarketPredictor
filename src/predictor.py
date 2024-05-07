# src/predictor.py
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def train_and_predict(df):
    """Train a model and predict future values with details."""
    # Suponha que usamos apenas os preços de fechamento para previsão
    df['target'] = df['close'].shift(-1)  # prever o próximo valor de fechamento
    df.dropna(inplace=True)

    X = df[['close']]
    y = df['target']
    model = LinearRegression()
    model.fit(X[:-1], y[:-1])  # Use all but the last point to train

    # Fazendo previsão para o último ponto e um ponto futuro
    last_point = np.array([[df['close'].iloc[-1]]])
    next_predicted_point = model.predict(last_point)
    future_point = model.predict([[next_predicted_point[0] + (next_predicted_point[0] - df['close'].iloc[-2])]])

    # Calculando erro percentual
    test_prediction = model.predict(X[-2:-1])
    error_percentage = (abs(test_prediction - y[-2:-1].values) / y[-2:-1].values) * 100

    recommendation = "comprar" if next_predicted_point > last_point else "vender"
    time_to_act = "imediatamente" if error_percentage < 10 else "monitorar mais"

    return {
        'current_value': df['close'].iloc[-1],
        'next_predicted_value': next_predicted_point[0],
        'future_predicted_value': future_point[0],
        'recommendation': recommendation,
        'time_to_act': time_to_act,
        'error_percentage': error_percentage[0]
    }