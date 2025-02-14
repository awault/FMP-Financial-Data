import os
import pandas as pd
import requests
from dotenv import load_dotenv
load_dotenv()

# Check if API key is available
from src.downloader import check_api_key
check_api_key()

# Fetch Data for AAPL
from src.downloader import fetch_fmp_data
data = fetch_fmp_data('AAPL')
print('\n')
print(data.head())
