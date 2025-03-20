import pandas as pd
data = [1, 2, None, 4] # python list
indexed_data = pd.Series(data=data, index=['d0', 'd1', 'd2', 'd3'])
print(indexed_data)