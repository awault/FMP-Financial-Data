# Functions used to download data

import os
from dotenv import load_dotenv
load_dotenv()


def check_api_key():
    """ Check if FMP API key is available in the environment variables."""
    fmp_api = os.getenv("FMP_API_KEY")
    if fmp_api:
        print("API key is available.")
        return True
    else:
        print("API key is missing. Please set key value in the environment variables.")
        return False