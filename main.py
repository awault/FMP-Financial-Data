# ./main.py

import os
import pandas as pd
import requests
import sqlite3
from dotenv import load_dotenv
load_dotenv()

# ANSI escape codes for text format

BLUE = '\033[34m'
CYAN = '\033[36m'
GREEN = '\033[32m'
MAGENTA = '\033[35m'
RED = '\033[31m'
YELLOW = '\033[33m'

BOLD = '\033[1m'
RESET = '\033[0m'

print(f"\n{BOLD}---- FMP Financial Data ----{RESET}\n")

# Check if API key is available
from src.downloader import check_api_key
check_api_key()

# Import fetch fmp data function
from src.downloader import fetch_fmp_data

# Define the main function to fetch data
def main():
    print(f"\n{BOLD}Select an option to fetch stock price data:{RESET}\n")
    print("1. Enter a single ticker")
    print("2. Enter a custom list of tickers")
    print("3. Fetch the NASDAQ 100")

    choice = input(f"\n{BOLD}Enter your choice: {RESET}").strip()

    if choice == "1":
        tickers = [input(f'\n{BOLD}Enter a single ticker: {RESET}').strip().upper()]

    elif choice == "2":
        tickers = input(f'\n{BOLD}Enter tickers separated by commas: {RESET}').strip().upper().split(",")

    elif choice == "3":
        print(f"\n{BOLD}Fetching the NASDAQ 100...{RESET}")
        # Import fetch_nasdaq_100 only if option 3 is selected
        from src.downloader import fetch_nasdaq_100
        tickers = fetch_nasdaq_100()

    else:
        print(f"\n{RED}Invalid choice. Exiting program.{RESET}\n")
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
            print(f'{BOLD}Original DataFrame{RESET}')
            print(all_data.info())
            print('\n')
            
            if invalid_tickers:
                print(f'\n{RED}The following tickers are invalid:{invalid_tickers}{RESET}\n')
            
            return all_data
            
    else:
        print(f"{RED}Failed to fetch data for the provided tickers.{RESET}")
        return None

# Call the main function and assign results to data_frame
data_frame = main()

# Import column cleaning function
from src.formatter import convert_to_snake_case

# Define a function to clean and format data
def clean_and_format(pandas_df):

    # Convert column names to snake_case
    pandas_df.columns = pandas_df.columns.map(convert_to_snake_case)

    # Select unnecessary columns
    columns_to_drop = ['change','change_percent','vwap','label','change_over_time','volume','unadjusted_volume']
    
    # Drop columns
    pandas_df = pandas_df.drop(columns=columns_to_drop,errors='ignore')

    # Convert date column to datetime
    pandas_df['date'] = pd.to_datetime(pandas_df['date'])

    print(f'\n{GREEN}Clean Column Names: {list(pandas_df.columns)}{RESET}\n')

    return pandas_df

clean_data = clean_and_format(data_frame)

print(f"{BOLD}Updated DataFrame{RESET}")
print(clean_data.info())


print(f'\n{BOLD}Connecting to SQLite database...{RESET}')

try:
    # Connect to SQLite
    conn = sqlite3.connect('fin_data.db')

    print(f'\nInserting data into daily_price table...')
    
    # Insert DataFrame into SQLite
    clean_data.to_sql('daily_price',conn,if_exists='replace',index=False)

    print("\nData has been successfully added to the database.")

except Exception as e:
    print(f"\n{RED}Error: {e} {RESET}")

finally:
    if conn:
        conn.close()



# Save data to csv file
# px_data.to_csv('px_data.csv',index=False)

