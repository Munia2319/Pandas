import pandas as pd

df = pd.read_csv('data.csv')


print('Printing dataframe with empty values')

print(df.head(20))

print('Printing dataframe after replcing empty values with mean of the column')
x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True)
print(df.head(20))
