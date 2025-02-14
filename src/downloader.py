# Functions used to download data

import os
import pandas as pd
import requests
from dotenv import load_dotenv
load_dotenv()

# Retrieve API key from the environment
FMP_API_KEY = os.getenv("FMP_API_KEY")

def check_api_key():
    """ Check if FMP API key is available in the environment variables."""
    fmp_api = os.getenv("FMP_API_KEY")
    if fmp_api:
        print("API key is available.")
        return True
    else:
        print("API key is missing. Please set key value in the environment variables.")
        return False

def fetch_fmp_data(ticker):
    url= f'https://financialmodelingprep.com/api/v3/historical-price-full/{ticker}?apikey={FMP_API_KEY}'
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if 'historical' in data:
            #Flatten historical list into a DataFrame
            historical_data = pd.DataFrame(data['historical'])
            return historical_data
        
        elif isinstance(data,dict):
            return pd.DataFrame([data])
        
        else:
            print("Unexpected data format received")

    except requests.RequestException as e:
        print(f'Error fetching data: {e}')
