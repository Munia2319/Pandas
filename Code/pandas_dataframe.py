import pandas as pd

df = pd.read_csv('data.csv')
print('Printing head of the dataset')

print(df.head(10))
print('Printing tail of the dataset')
print(df.tail(10))
print('Printing info of the dataset')
print(df.info()) 
