import pandas as pd
import matplotlib.pyplot as plt

vehicle_product =  'https://github.com/dongupak/DataML/raw/main/csv/vehicle_prod.csv'
df = pd.read_csv(vehicle_product,index_col=0)
print(df)
print()
print(df.tail())    # 데이터가 많을 때 뒤 쪽을 봄
print()
print(df[0:3])      # 데이터의 한 부분만 볼 수 있음
print()
data_k = df.loc['Korea']
print(data_k)
print()
data2 = df.loc[['Korea','US']] # 2개 이상을 보고 싶다면 이렇게
print(data2)
print()
print(df.iloc[4])   #Korea 보는것
print()
print(df.iloc[2,4]) # 인데스 2 의 4번째 요소 US에 4번째
print(df.iloc[2:4]) # US 가 2 이고 JAPAN이 3이니 4전에 3까지 다 나타냄

"""
1. head(),tail() 메소드 : 첫, 마지막 항목 중에서 지정된 개수를 가져올 수 있다.
2. [m,n]을 사용 : 지정된 구간 m,n의 항목을 가져올 수 있다.
3. loc[] : 인덱스에서 특정 레이블이 있는 행을 가져온다.
4. iloc[]: 인덱스에서 정수형 인덱스를 사용하여 특정 위치에 있는 행을 가져온다.
"""