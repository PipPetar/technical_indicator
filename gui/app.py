"""
app.py
Defines the Tkinter-based GUI for displaying financial data and indicators.
"""


import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from data.fetch import get_data
from indicators.sma import apply_sma
from indicators.ema import apply_ema
from indicators.rsi import apply_rsi
from indicators.bollinger import apply_bollinger


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("YFinance GUI")

        # Ticker input
        tk.Label(self, text="Ticker:").grid(row=0, column=0, padx=5, pady=5)
        self.ticker_var = tk.StringVar(value="AAPL")
        tk.Entry(self, textvariable=self.ticker_var).grid(row=0, column=1, padx=5, pady=5)

        # Year dropdown
        tk.Label(self, text="Years:").grid(row=1, column=0, padx=5, pady=5)
        self.years_var = tk.IntVar(value=1)
        ttk.Combobox(self, textvariable=self.years_var, values=[1,2,3,4,5]).grid(row=1, column=1, padx=5, pady=5)

        # Indicators checkboxes
        self.sma_var = tk.BooleanVar()
        self.ema_var = tk.BooleanVar()
        self.rsi_var = tk.BooleanVar()
        self.boll_var = tk.BooleanVar()

        tk.Checkbutton(self, text="SMA", variable=self.sma_var).grid(row=2, column=0, padx=5, pady=5)
        tk.Checkbutton(self, text="EMA", variable=self.ema_var).grid(row=2, column=1, padx=5, pady=5)
        tk.Checkbutton(self, text="RSI", variable=self.rsi_var).grid(row=3, column=0, padx=5, pady=5)
        tk.Checkbutton(self, text="Bollinger", variable=self.boll_var).grid(row=3, column=1, padx=5, pady=5)

        # Plot button
        tk.Button(self, text="Plot", command=self.plot_data).grid(row=4, column=0, columnspan=2, pady=10)

    def plot_data(self):
        ticker = self.ticker_var.get()
        years = self.years_var.get()
        df = get_data(ticker, years)

        # Apply indicators
        if self.sma_var.get():
            df = apply_sma(df)
        if self.ema_var.get():
            df = apply_ema(df)
        if self.rsi_var.get():
            df = apply_rsi(df)
        if self.boll_var.get():
            df = apply_bollinger(df)

        # Plot
        fig, ax = plt.subplots(figsize=(6,4))
        ax.plot(df["Close"], label="Close")
        if self.sma_var.get():
            ax.plot(df["SMA"], label="SMA")
        if self.ema_var.get():
            ax.plot(df["EMA"], label="EMA")
        if self.boll_var.get():
            ax.plot(df["BB_upper"], label="BB Upper")
            ax.plot(df["BB_lower"], label="BB Lower")
        ax.set_title(f"{ticker} Price Chart")
        ax.legend()

        # Show plot in Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().grid(row=5, column=0, columnspan=2)
        canvas.draw()
