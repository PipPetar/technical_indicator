import yfinance as yf

def get_data(ticker, years=1):
    period = f"{years}y"
    df = yf.download(ticker, period=period)
    return df.dropna()
