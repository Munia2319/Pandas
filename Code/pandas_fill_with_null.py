import pandas as pd

df = pd.read_csv('data.csv')


print('Printing dataframe with empty values')

print(df.head(20))
df.dropna(inplace=True)
print('Printing dataframe after dropping empty rows with Null values')
print(df.head(20))
