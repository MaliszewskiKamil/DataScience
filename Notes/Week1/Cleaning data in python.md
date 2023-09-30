https://campus.datacamp.com/courses/cleaning-data-in-python
#bigdata
example: 21503$
get data types of columns with:
```python
df.dtypes
df.info()
```

To find rows with a $ sign we can use:
```python
#na=False replaces all NaN values with False
df[df['column'].str.contains('$', na=False)]
```
to remove the $ sign we can use
```python
df['column'] = df['column'].str.strip('$')'
#and now we can change it to int:
df['column'] = df['column'].astype('int')
	
#verify that df is now an integer
assert df['column'].dtype == 'int'
```
#assert is very important for testing

![](../images/w1/Pasted%20image%2020230930195334.png)


![[Pasted image 20230927165545.png]]
![[Pasted image 20230927165609.png]]


changing type is good when we need a good description of a specific category

Data can be sometimes out of range due to human error, what we can do about that is:
dropping data (but be really careful about that)
setting custom minimums and maximums
Treat as missing and impute
Setting custom value depending on business assumptions

so if something like that happen, we can do the following
```python
movies = movies[movies['avg_rating'] <= 5] #create a new dataframe
#or drop values using .drop()
movies.drop(movies['avg_rating'] > 5]. index, inplace = True)
#now its important to test it
assert movies['avg_rating'].max() <= 5

#another option is to set the value to the max value
movies.loc[movies['avg_rating'] > 5, 'avg_rating'] = 5
```


