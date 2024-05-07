# main.py
import tkinter as tk
from src.interface import FinancialPredictorInterface

def main():
    root = tk.Tk()
    app = FinancialPredictorInterface(master=root)
    app.mainloop()

if __name__ == '__main__':
    main()
