import pandas as pd

income = {'1월' : 9500, '2월' : 6200, '3월' : 6050, '4월':7000}
income_se = pd.Series(income)
print('동윤이네 상점의 수익')
print(income_se)