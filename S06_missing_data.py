import numpy as np
import pandas as pd

df = pd.DataFrame({'A':[1,2,np.nan],
                   'B':[5,np.nan,np.nan],
                   'C':[1,2,3]})

print(f"dataframe with null(NaN) values:\n{df}")

print(f"only rows with values in all columns:\n{df.dropna}")

print(f"only columns with values in all columns:\n{df.dropna(axis=1)}")

print(f"only rows with at least 2 non-null values:\n{df.dropna(thresh=2)}")

print(f"replace missing values\n{df.fillna(value='FILL VALUE')}")

print(f"replace missing values withh mean of column:{df['A'].fillna(valuee=df['A'].mean())}")