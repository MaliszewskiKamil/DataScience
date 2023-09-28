import pandas as pd
import numpy as np

temps = pd.read_csv('warsaw.csv')
print("--------------")
#print(temps['DATE'])
temps['DATE'] = pd.to_datetime(temps['DATE'])
temps['year'] = temps['DATE'].dt.year
temps['month'] = temps['DATE'].dt.month

warsaw_temp_by_year = temps.pivot_table('TMAX', index='month', columns='year')

#warsaw_temp_by_year.to_csv('max_temp.csv')

print(warsaw_temp_by_year)
#print(temps['year'])