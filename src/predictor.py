# src/predictor.py

def predict(data):
    """Example prediction function using the last close price."""
    # Exemplo simples: retornar o último preço de fechamento como "previsão"
    last_close_price = data['close'].iloc[-1]
    return last_close_price
