import pandas as pd
import os

# save filepath to variable for easier access
melbourne_file_path = '.\\input\\melbourne-housing-snapshot\\melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)
print(" ")

print(melbourne_data.shape)
print(" ")

print(type(melbourne_data))
print(" ")

# print a summary of the data in Melbourne data
a = melbourne_data.describe()
print(a)
print(" ")

# print the 'Mean' of the 'Price'
# using indexing, row first, colunm second
print(a.loc['mean']['Price'])
print(a.loc['mean'][1])  # same
print(" ")  # loc for string

print(a.iloc[1][1])
print(a.iloc[1]['Price'])  # same
print(" ")  # iloc for number

# print the 'Mean' of the 'Price'
# using pandas Native accessors,
# column first, row second
print(a['Price']['mean'])
print(a['Price'][1])  # same
print(" ")

# loc include, 0 to 10 means 0 to 10
print(a.loc['mean']['Rooms':'Price'])
print(" ")

# iloc exclude, 0 to 10 means 0 to 9
print(a.iloc[1][0:1])
print(" ")

# condition select
print(a.loc[a['Rooms'] == 3])

