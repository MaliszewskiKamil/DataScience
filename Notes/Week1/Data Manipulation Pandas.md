https://campus.datacamp.com/courses/data-manipulation-with-pandas

pip packages are stored in site-packages folder

example dataframe called homelessness:
homelessness.head()
homelessness.info()
homelessness.describe()
homelessness.

![[Pasted image 20230925112323.png]]
![[Pasted image 20230925112509.png]]
df['column'].agg(custom_function)
allows for using my own fuctions that i may want to create to find specifics inside the data. example:
*********************
# A custom IQR function
def iqr(column):

    return column.quantile(0.75) - column.quantile(0.25)
# Print IQR of the temperature_c column
print(sales['temperature_c'].agg(iqr))

***********************
Importing multiple aggregation functions looks like this:
![[Pasted image 20230925114622.png]]
df.drop_duplicates(subset='column')


-----------------------------
matplotlib:
histogram good for looking how distribution looks like
histogram = df['col'].hist(bins=4)

bins -> nr of bars
plt.show()

barplots can show relations between a categorical and numerical variables, like avarage wage of type of dog
.plot(kind="bar", title="Dogs names")

Line plots:
good for visualing changes in numeric value over time. (weight over time for example)

.plot(x="date", y='weigth_kg', kind='line', rot=45)
rot = rotation of labels text in degrees

Scatter plots good for finding relationship between two numeric values, like height and weight.

Layering plots is also possible (for example male vs female)

![[Pasted image 20230927110744.png]]

--------------

<h1>Missing Values </h1>
df.isna() -> searches if there are missing values
df.isna().any() -> checks for all columns
df.isna().sum() -> sums amount of missing values in column

we can plot missing values as well:
df.isna().sum().plot(kind='bar')

to remove rows with missing values (not ideal) 
df.dropna()

replace missing values 
df.fillna(0)

------------------------------
<h1>Dataframes</h1>
<h2>Dictionaries</h2>
my_dict = {
	'key1': value1,
	'ley2': value2,
	'key3': value3
}

Dataframes can be created in two ways, from a list of dictionaries (by row) or from a dictionary of lists (by columns)
![[Pasted image 20230927115724.png]]

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

<h2>Writing/Reading CSV</h2>
pd.read_csv("file.csv")
newpd_to_csv(new_file.csv)