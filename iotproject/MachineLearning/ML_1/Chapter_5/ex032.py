import pandas as pd
import numpy as np

s_a = pd.Series([1, 2, np.nan, 4])  #np.nan 은 결측값
print(s_a)
print(type(s_a))
print(s_a[0])
print(s_a.isna())