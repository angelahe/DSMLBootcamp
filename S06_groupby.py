import pandas as pd

# create dataframe
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
        'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)
print(f"dataframe is:\n{df}")

by_company = df.groupby('Company')

# get sum, average, std deviations as dataframe
print(f"total sales by company:\n{by_company.sum()}")

print(f"average sales by company:\n{by_company.mean()}")

print(f"standard deviations by company:\n{by_company.std()}")

print(f"total sales for FB: {by_company.sum().loc['FB']}")

print(f"total sales for FB in one line: {df.groupby('Company').sum().loc['FB']}")

print(f"count of people and sales per company: {df.groupby('Company').count()}")

print(f"max salesperson (alpha) per company: {df.groupby('Company').max()}")

print(f"min salesperson (alpha)per company: {df.groupby('Company').min()}")

print(f"describe for info on dataset: {df.groupby('Company').describe()}")

print(f"describe for info on dataset: {df.groupby('Company').describe().transpose()}")

print(f"transposed describe info on GOOG: {by_company.describe().transpose()['GOOG']}")