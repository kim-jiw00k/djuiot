import pandas as pd
import matplotlib.pyplot as plt

vehicle_product =  'https://github.com/dongupak/DataML/raw/main/csv/vehicle_prod.csv'
print(vehicle_product)
print()
df = pd.read_csv(vehicle_product,index_col=0)
df = df.transpose()      # row 랑 column이 바뀜
print(df)

df.plot.line()
plt.show()