import seaborn as sns
titanic=sns.load_dataset('titanic')
print(type(titanic))
print(titanic.head())
print(titanic.info())
print(titanic.describe())
titanic.columns
data=titanic[['survived','age']]
print(data)
addn=data+10
print(addn.head())