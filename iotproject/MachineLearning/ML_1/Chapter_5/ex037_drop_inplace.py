import pandas as pd

d_df = pd.DataFrame(data = [[10, 20, 30, 40],[50, 60, 70, 80]],columns=['A','B','C','D'])
print(d_df)
print()

new_df = d_df.drop('B',axis=1,inplace=False) #원본 변경 불가
print(new_df)
print()

print(d_df.drop('B', axis=1, inplace=True)) #원본 변경
print(d_df)