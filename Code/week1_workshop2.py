import matplotlib as plt
import numpy as np
import pandas as pd

movies = pd.read_csv('IMDb movies.csv')
print(movies.head())

#print(movies.columns)
#print(movies.info())
#print(movies.describe())(
print(movies.dtypes)

#print(movies[(movies == '$').any(axis=1)])
movies_with_dollar = movies[movies['budget'].str.contains('$')]

print(movies_with_dollar.head())
movies_with_dollar['budget'] = movies_with_dollar.loc[movies_with_dollar['budget'].str.strip('$', na=False)]




#print(movies.loc[movies[movies['budget'].str.contains('$', na=False)]])