"""
rsi.py
Implements the Relative Strength Index (RSI) calculation.
"""


def apply_rsi(df, window=14):
    delta = df["Close"].diff()
    up = delta.clip(lower=0).rolling(window).mean()
    down = (-delta.clip(upper=0)).rolling(window).mean()
    rs = up / down
    df["RSI"] = 100 - (100 / (1 + rs))
    return df
