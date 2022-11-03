import pandas as pd

df = pd.read_csv('data.csv')


print('Printing dataframe with empty values')

print(df.head(20))

print('Printing dataframe after removing duplicate values')
df.drop_duplicates(inplace = True)
print(df.head(20))
