import pandas as pd

# create dataframe
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
        'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)
print(f"dataframe is:\n{df}")

by_company = df.groupby('Company')

print(f"total sales by company:\n{by_company.sum()}")

print(f"mean sales by company:\n{by_company.mean()}")
