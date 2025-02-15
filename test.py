# Use this file to test operation of functions in terminal

from src.downloader import fetch_nasdaq_100

if __name__ == "__main__":
    tickers = fetch_nasdaq_100()
    print(tickers)
