import pandas as pd
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})

print(f"dataframe:\n{df.head()}")

# find unique values in a dataframe

print(f"unique values in column2: {df['col2'].unique()}")
print(f"# of unique values in col2:{len(df['col2'].unique())}")
print(f"# of unique values in col2 method2:{df['col2'].nunique()}")
print(f"unique values and how many times they show up:\n{df['col2'].value_counts()}")

# selecting data
#Select from DataFrame using criteria from multiple columns

print(f"return data where val in col1 > 2:\n{df[df['col1']>2]}")
print(f"remember this is just returning a series of true and false:\n{df['col1']>2}")
newdf = df[(df['col1']>2) & (df['col2']==444)]
print(f"where col1 > 2 and col2 is 444\n{newdf}")