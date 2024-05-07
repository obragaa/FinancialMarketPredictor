import tkinter as tk
from tkinter import messagebox, simpledialog
from src.data_manager import fetch_financial_data, process_financial_data, save_data_to_csv
from src.predictor import predict
from src.config import API_KEY, BASE_URL  # Importa configurações

class FinancialPredictorInterface(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        self.get_data_btn = tk.Button(self, text="Obter Dados", command=self.get_financial_data)
        self.get_data_btn.pack()

        self.predict_btn = tk.Button(self, text="Prever", command=self.make_prediction)
        self.predict_btn.pack()

        self.quit_btn = tk.Button(self, text="Sair", fg="red", command=self.master.destroy)
        self.quit_btn.pack()

    def get_financial_data(self):
        symbol = simpledialog.askstring("Input", "Qual o símbolo da ação?", parent=self)
        if symbol:
            data, interval = fetch_financial_data(symbol)  # Receber dados e interval
            processed_data = process_financial_data(data, interval)  # Passar interval
            self.processed_data = processed_data
            messagebox.showinfo("Informação", "Dados obtidos com sucesso!")


    def make_prediction(self):
        if hasattr(self, 'processed_data'):
            result = predict(self.processed_data)
            messagebox.showinfo("Previsão", f"Resultado da Previsão: {result}")
        else:
            messagebox.showerror("Erro", "Dados não disponíveis. Por favor, obtenha os dados primeiro.")

# Código para iniciar a interface estará em main.py
