import tkinter as tk
from tkinter import Toplevel, Label, Button, simpledialog, font
from src.data_manager import fetch_financial_data, process_financial_data, save_data_to_csv
from src.predictor import train_and_predict

class FinancialPredictorInterface(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg='white')  # Background branco para a janela principal
        self.master.title("Financial Market Predictor")
        self.master.geometry("500x140")
        self.pack(fill='both', expand=True)
        self.create_widgets()

    def create_widgets(self):
        widget_font = font.Font(family="Helvetica", size=12, weight="bold")
        self.get_data_btn = tk.Button(self, text="Obter e Prever", command=self.get_and_predict,
                                      font=widget_font, bg='#4CAF50', fg='white')
        self.get_data_btn.pack(pady=20, padx=20, fill='x')
        self.quit_btn = tk.Button(self, text="Sair", command=self.master.destroy,
                                  font=widget_font, bg='#f44336', fg='white')
        self.quit_btn.pack(pady=10, padx=20, fill='x')

    def get_and_predict(self):
        symbol = simpledialog.askstring("Input", "Qual o símbolo da ação?", parent=self)
        if symbol:
            data, interval = fetch_financial_data(symbol)
            processed_data = process_financial_data(data, interval)
            save_data_to_csv(processed_data, symbol)
            prediction = train_and_predict(processed_data)
            self.show_custom_messagebox(prediction)

    def show_custom_messagebox(self, prediction):
        # Janela customizada para a mensagem de previsão
        popup = Toplevel(self)
        popup.title("Previsão Detalhada")
        popup.geometry("400x200")
        popup.configure(bg='white')
        
        # Estilizando a mensagem
        message_font = font.Font(family="Helvetica", size=10)
        Label(popup, text=f"Previsão atual: {prediction['current_value']}",
              bg='white', fg='#333', font=message_font).pack(pady=(10, 0))
        Label(popup, text=f"Próxima previsão: {prediction['next_predicted_value']}",
              bg='white', fg='green' if prediction['next_predicted_value'] > prediction['current_value'] else 'red',
              font=message_font).pack()
        Label(popup, text=f"Previsão futura: {prediction['future_predicted_value']}",
              bg='white', fg='green' if prediction['future_predicted_value'] > prediction['current_value'] else 'red',
              font=message_font).pack()
        Label(popup, text=f"Recomendação: {prediction['recommendation']} ({prediction['time_to_act']})",
              bg='white', fg='blue', font=message_font).pack()
        Label(popup, text=f"Erro percentual estimado: {prediction['error_percentage']:.2f}%",
              bg='white', fg='orange', font=message_font).pack(pady=(0, 10))
        
        Button(popup, text="Fechar", command=popup.destroy,
               bg='#f44336', fg='white', font=message_font).pack(pady=(10, 0), fill='x')

if __name__ == '__main__':
    root = tk.Tk()
    app = FinancialPredictorInterface(master=root)
    app.mainloop()
