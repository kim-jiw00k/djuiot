import numpy as np

ary1 = np.arange(1, 10)
print(ary1)
print(ary1.max())   # 최대값
print(ary1.min())   # 최소값
print(ary1.mean())  # 평균값

ary2 = ary1.astype(np.float32)      # tensorflow에선 디폴트가 32비트
print(ary2)                         # astype 쓰면 좋음