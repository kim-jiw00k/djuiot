import pandas as pd
import matplotlib.pyplot as plt

vehicle_product =  'https://github.com/dongupak/DataML/raw/main/csv/vehicle_prod.csv'
print(vehicle_product)
print()
df = pd.read_csv(vehicle_product)
print(type(df))
print()
print(df)
print()
print(df.columns)
print()
print(df.index)
print()
df = pd.read_csv(vehicle_product, index_col=0)
print(df)
print()
print(df['2007'])
print()
list_columns = df.columns.tolist()          # 파이썬 리스트로 바꿈
print(list_columns)
print()
list_of_2007 = df['2007'].tolist()          # 파이썬 리스트로 바꿈
print(list_of_2007)
print()
df['Total'] = df.sum(axis=1)                # total 을 만듦
print(df)
print()

df['Mean'] = df[['2007','2008','2009','2010','2011']].mean(axis=1)  # total을 뺀 평균 값 구함
print(df)
print()

df.drop('2007',axis=1)      # 원본 수정(x) Binding(x)
print(df)
print()
df.drop('2007',inplace=True,axis=1) #원본 수정 (O) Binding(X)
df['Total'] = df[['2008','2009','2010','2011']].sum(axis=1)
df['Mean'] = df[['2008','2009','2010','2011']].mean(axis=1)
print(df)
print()

df.drop('Mexico', axis=0,inplace=True)
print(df)

df['2009'].plot(kind='bar', color=('orange','r','b','m','c','k'))
plt.show()