import pandas as pd
import os

# save filepath to variable for easier access
melbourne_file_path = '.\\input\\melbourne-housing-snapshot\\melb_data.csv'

melbourne_data = pd.read_csv(melbourne_file_path)

print(type(melbourne_data))

print(melbourne_data.describe())

a = melbourne_data.describe()

# print the 'Mean' of the 'Price'
print(a.loc['mean']['Price'])
