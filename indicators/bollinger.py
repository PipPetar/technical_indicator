def apply_bollinger(df, window=20):
    ma = df["Close"].rolling(window).mean()
    sd = df["Close"].rolling(window).std()
    df["BB_upper"] = ma + 2 * sd
    df["BB_lower"] = ma - 2 * sd
    return df
