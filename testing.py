# testing.py
# This is a file to test python scripts

import pandas as pd
from src.formatter import convert_to_snake_case
from src.formatter import drop_columns

test_data = pd.read_csv('px_data.csv')

print(test_data.info())
print(test_data.head())

test_data.columns = test_data.columns.map(convert_to_snake_case)

drop_columns(test_data)