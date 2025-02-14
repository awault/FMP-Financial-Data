import os
import pandas as pd
import requests
from dotenv import load_dotenv
load_dotenv()

FMP_API_KEY = os.getenv("FMP_API_KEY")
print(FMP_API_KEY)