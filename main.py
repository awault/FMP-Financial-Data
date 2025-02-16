# ./main.py
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

def main():
    print("\nSelect an option to fetch stock price data:\n")
    print("1. Enter a single ticker")
    print("2. Enter a custom list of tickers")
    print("3. Fetch the NASDAQ 100")

    choice = input("\nEnter your choice:\n").strip()

    if choice == "1":
        tickers = [input('Enter a single ticker:').strip().upper()]

    elif choice == "2":
        tickers = input('Enter tickers separated by commas: ').strip().upper().split(",")

    elif choice == "3":
        # Import fetch_nasdaq_100 only if option 3 is selected
        from src.downloader import fetch_nasdaq_100
        tickers = fetch_nasdaq_100()

    else:
        print("\nInvalid choice. Exiting program.\n")
        return
    
    # Create an empty DataFrame and empty list
    all_data = pd.DataFrame()
    invalid_tickers = []

    # Fetches data for the selected stocks
    for ticker in tickers:
        print(f"\nFetching data for {ticker}...")
        df = fetch_fmp_data(ticker)
        
        if df is not None and not df.empty:
            df['symbol'] = ticker
            all_data = pd.concat([all_data,df], ignore_index=True)

        else:
            invalid_tickers.append(ticker)
            
    if not all_data.empty:
            print(all_data.info())
            
            if invalid_tickers:
                print(f'\nThe following tickers are invalid:{invalid_tickers}\n')
            
            return all_data
            
    else:
        print(f"Failed to fetch data for the provided tickers.")
        return None

px_data = main()

