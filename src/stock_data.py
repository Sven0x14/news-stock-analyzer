import yfinance as yf

def stock_prices_last_30_days(ticker):
    stock = yf.Ticker(ticker)

    try:
        data = stock.history(period="1mo")
    except Exception as e:
        raise RuntimeError(
            f"Failed to retrieve stock data for {ticker}"
        ) from e

    if data.empty:
        raise ValueError(
            f"No stock data available for {ticker}"
        )

    return data