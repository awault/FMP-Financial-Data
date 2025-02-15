print("\n ~~ FMP Stock Price Data ~~ \n")
import os
import pandas as pd
import requests
from dotenv import load_dotenv
load_dotenv()

# Check if API key is available
from src.downloader import check_api_key
check_api_key()

# Import fetch fmp data function
from src.downloader import fetch_fmp_data

# Import fetch NASDAQ 100
from src.downloader import fetch_nasdaq_100

def main():
    print("\nSelect an option to fetch stock price data:\n")
    print("1. Enter a single ticker")
    print("2. Enter a custom list of tickers")
    print("3. Fetch the NASDAQ 100")

    choice = input("\nEnter your choice:").strip()

    if choice == "1":
        tickers = [input('Enter a single ticker:').strip().upper()]

    elif choice == "2":
        tickers = input('Enter tickers separated by commas: ').strip().upper().split(",")

    elif choice == "3":
        tickers = fetch_nasdaq_100()

    else:
        print("\nInvalid choice. Exiting program.\n")
        return
    
    all_data = pd.DataFrame()

    for ticker in tickers:
        print(f"\nFetching data for {ticker}...")
        df = fetch_fmp_data(ticker)
        
        if df is not None and not df.empty:
            df['symbol'] = ticker
            all_data = pd.concat([all_data,df], ignore_index=True)
            
    if not all_data.empty:
            print(all_data.head())
            
    else:
        print(f"Failed to fetch data for the provided tickers.")



if __name__ == "__main__":
    main()