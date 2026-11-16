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
df['per_unit'] = df['revenue'] / df['quanity']
print(df.head())

print("-----Exercise 6-----")
print(df['region'].unique())
print(df['region'].value_counts())

print("-----Exercise 7-----")
df_subset = df[['region','product','revenue']]
print(df_subset.shape)

print("-----Exercise 8-----")
test