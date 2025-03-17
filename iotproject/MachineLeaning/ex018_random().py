import numpy as np
a = np.random.randint(150, 191, size= 10)
print(a)

#randn 은 normalization 정규화

rnd = np.random.randn(5) * 10 + 165 #평균값이 165, 표준편차가 10인 값
print(rnd)