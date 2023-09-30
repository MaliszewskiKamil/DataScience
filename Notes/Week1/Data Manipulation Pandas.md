	https://campus.datacamp.com/courses/data-manipulation-with-pandas
#bigdata 
pip packages are stored in site-packages folder
```python
#example dataframe called homelessness:
homelessness.head()
homelessness.info()
homelessness.describe()
```

![](../Pasted%20image%2020230930195723.png)
![](../Pasted%20image%2020230930195731.png)
```python
df['column'].agg(custom_function)
```
allows for using my own fuctions that i may want to create to find specifics inside the data. example:
*********************
```python
# A custom IQR function
def iqr(column):

    return column.quantile(0.75) - column.quantile(0.25)
# Print IQR of the temperature_c column
print(sales['temperature_c'].agg(iqr))
```

***********************
Importing multiple aggregation functions looks like this:
![](../Pasted%20image%2020230930195750.png)
```python
df.drop_duplicates(subset='column')
```

-----------------------------
matplotlib:
histogram good for looking how distribution looks like
```python
histogram = df['col'].hist(bins=4)
plt.show()
```

bins -> nr of bars

barplots can show relations between a categorical and numerical variables, like avarage wage of type of dog
```python
.plot(kind="bar", title="Dogs names")
```


Line plots:
good for visualing changes in numeric value over time. (weight over time for example)
```python
.plot(x="date", y='weigth_kg', kind='line', rot=45)
```
rot = rotation of labels text in degrees

Scatter plots good for finding relationship between two numeric values, like height and weight.

Layering plots is also possible (for example male vs female)

![](../Pasted%20image%2020230930195804.png)

--------------

# Missing Values

```python
df.isna()  #searches if there are missing values
df.isna().any() # checks for all columns
df.isna().sum() # sums amount of missing values in column

#we can plot missing values as well:
df.isna().sum().plot(kind='bar')

#to remove rows with missing values (not ideal) 
df.dropna()

#replace missing values 
df.fillna(0)

```


------------------------------
# Dataframes

## Dictionaries

```python
my_dict = {
	'key1': value1,
	'ley2': value2,
	'key3': value3
}
```


Dataframes can be created in two ways, from a list of dictionaries (by row) or from a dictionary of lists (by columns)
![](../Pasted%20image%2020230930195813.png)

```python
list_of_dicts = [
	{'name': 'Ginger', 'breed': "JRT", 'height': 22, 'weight': 10, 'date_of_birth': '2019-03-14'}
	{'name': 'Bob', 'breed': "Sznaucer", 'height': 16, 'weight': 7, 'date_of_birth': '2015-08-14'}
]
new_dogs = pd.DataFrame(list_of_dicts)

dict_of_lists = {
	"name": ["Ginger", "Bob"],
	"breed": ['JRT', 'Sznaucer']
	etc.etc.
}
```


## Writing/Reading CSV

```python
pd.read_csv("file.csv")
newpd_to_csv(new_file.csv)
```
