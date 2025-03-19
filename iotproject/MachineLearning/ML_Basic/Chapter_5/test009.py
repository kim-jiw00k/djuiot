# 5장 pdf 13page
import numpy as np
import pandas as pd

month_se = pd.Series(['1월', '2월', '3월', '4월'])
income_se = pd.Series([9500, 6200, 6050, 7000])
expenses_se = pd.Series([5040, 2350, 2300, 4800])
df = pd.DataFrame({'월' : month_se, '수익': income_se, '지출':expenses_se})

print(df)

# 판다스 Series를 이용하여 최대 수익 월을 출력하기
m_index = np.argmax(income_se)  # 넘파이의 argmax() 사용
print('최대 수익이 발생한 월 : ', month_se[m_index])
print('월 최대 수익 : ',income_se.max(),'\n월 평균 수익 : ',income_se.mean())

income_sum = np.sum(income_se)
expenses_sum = np.sum(expenses_se)
print("동윤이네 상점의 수입 합계 : {:,}".format(income_sum))       # 1000 단위에 , 붙이기
print("동윤이네 사점의 지출 합계 : {:,}".format(expenses_sum))     # 1000 단위에 , 붙이기