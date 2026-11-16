import pandas as pd 
df = pd.read_csv('retail_sales.csv')

#imports pandas and reads it 
print("-----Exercise 1-----")
print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)


print("-----Exercise 2-----")
south=df[df['region']=='South']
print(len(south))
print(south.head())

print("-----Exercise 3-----")
top_5=df.sort_values('revenue', ascending=False).head(5)
print(top_5)

print("-----Exercise 4-----")
big_south=df[(df['region'] == 'South') &(df['revenue'] > 1000)]

print("-----Exercise 5-----")
