def apply_sma(df, window=20):
    df["SMA"] = df["Close"].rolling(window).mean()
    return df
