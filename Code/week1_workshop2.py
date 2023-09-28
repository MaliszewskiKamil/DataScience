import matplotlib as plt
import numpy as np
import pandas as pd

movies = pd.read_csv('IMDb movies.csv')
print(movies.head())

print(movies.columns)
print(movies.info())
print(movies.describe())

print(movies.loc[movies[movies['budget'].str.contains('$', na=False)]])