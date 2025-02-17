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

# Define the main function to fetch data
def main():
    print("\nSelect an option to fetch stock price data:\n")
    print("1. Enter a single ticker")
    print("2. Enter a custom list of tickers")
    print("3. Fetch the NASDAQ 100")

    choice = input("\nEnter your choice: ").strip()

    if choice == "1":
        tickers = [input('\nEnter a single ticker: ').strip().upper()]

    elif choice == "2":
        tickers = input('\nEnter tickers separated by commas: ').strip().upper().split(",")

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
            print('\n')
            print('Original DataFrame')
            print('\n')
            print(all_data.info())
            print('\n')
            
            if invalid_tickers:
                print(f'\nThe following tickers are invalid:{invalid_tickers}\n')
            
            return all_data
            
    else:
        print(f"Failed to fetch data for the provided tickers.")
        return None

# Call the main function and assign results to data_frame
data_frame = main()

from src.formatter import convert_to_snake_case

def clean_and_format(pandas_df):

    # Convert column names to snake_case
    pandas_df.columns = pandas_df.columns.map(convert_to_snake_case)

    # List unnecessary columns
    columns_to_drop = ['change','change_percent','vwap','label','change_over_time','volume','unadjusted_volume']
    
    # Drop columns
    pandas_df = pandas_df.drop(columns=columns_to_drop,errors='ignore')

    # Convert date column to datetime
    pandas_df['date'] = pd.to_datetime(pandas_df['date'])


    
    print(f'\nCleaned Column Names: {list(pandas_df.columns)}\n')

    return pandas_df

clean_data = clean_and_format(data_frame)

print("Updated DataFrame")
print('\n')
print(clean_data.info())
print('\n')
print(clean_data.head())
print('\n')




# Save data to csv file
# px_data.to_csv('px_data.csv',index=False)

