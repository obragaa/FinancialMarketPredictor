import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, font, Toplevel, Label, Button
from src.data_manager import fetch_financial_data, process_financial_data, save_data_to_csv
from src.predictor import train_and_predict

class FinancialPredictorInterface(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg='white')
        self.master.title("Financial Market Predictor")
        self.master.geometry("500x300")
        self.pack(fill='both', expand=True)
        self.create_widgets()

    def create_widgets(self):
        widget_font = font.Font(family="Helvetica", size=12, weight="bold")
        self.ticker_combobox = ttk.Combobox(self, values=self.fetch_tickers(), font=widget_font)
        self.ticker_combobox.set("Selecione um ticker")  # Mensagem padrão
        self.ticker_combobox.pack(pady=20, padx=20, fill='x')

        self.get_data_btn = tk.Button(self, text="Obter e Prever", command=self.get_and_predict,
                                      font=widget_font, bg='#4CAF50', fg='white')
        self.get_data_btn.pack(pady=10, padx=20, fill='x')

        self.quit_btn = tk.Button(self, text="Sair", command=self.master.destroy,
                                  font=widget_font, bg='#f44336', fg='white')
        self.quit_btn.pack(pady=10, padx=20, fill='x')

    def fetch_tickers(self):
        # Retorna uma lista estática de tickers; substitua isso por uma chamada de API se necessário
        return ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'FB', 'TSLA']

    def get_and_predict(self):
        ticker = self.ticker_combobox.get()
        if ticker in self.fetch_tickers():
            data, interval = fetch_financial_data(ticker)
            processed_data = process_financial_data(data, interval)
            save_data_to_csv(processed_data, ticker)
            prediction = train_and_predict(processed_data)
            self.show_custom_messagebox(prediction)
        else:
            messagebox.showerror("Erro", "Por favor, selecione um ticker válido.")

    def show_custom_messagebox(self, prediction):
        popup = Toplevel(self)
        popup.title("Previsão Detalhada")
        popup.geometry("400x300")
        popup.configure(bg='white')

        message_font = font.Font(family="Helvetica", size=10)
        labels = [
            f"Valor atual: {prediction['current_value']}",
            f"Próxima previsão: {prediction['next_predicted_value']}",
            f"Previsão futura: {prediction['future_predicted_value']}",
            f"Recomendação: {prediction['recommendation']} ({prediction['time_to_act']})",
            f"Erro percentual estimado: {prediction['error_percentage']:.2f}%"
        ]
        for text in labels:
            Label(popup, text=text, bg='white', fg='#333', font=message_font).pack(pady=5)
        Button(popup, text="Fechar", command=popup.destroy, bg='#f44336', fg='white', font=message_font).pack(pady=10, fill='x')

if __name__ == '__main__':
    root = tk.Tk()
    app = FinancialPredictorInterface(master=root)
    app.mainloop()
