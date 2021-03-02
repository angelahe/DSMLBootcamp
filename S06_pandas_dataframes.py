# dataframes are bunch of series objects put together to share the same index

import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())

print(f'dataframe:\n{df}')
