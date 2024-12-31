def apply_ema(df, window=20):
    df["EMA"] = df["Close"].ewm(span=window).mean()
    return df