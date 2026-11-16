import pandas as pd 
df = pd.read_csv('retail_sales.csv')

#imports pandas and reads it 

print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)