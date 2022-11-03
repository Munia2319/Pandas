import pandas as pd

df = pd.read_csv('data.csv')

new_df = df.dropna()
print('Printing dataframe with empty values')

print(df.head(20))
print('Printing dataframe after dropping empty values values')
print(new_df.head(20))
