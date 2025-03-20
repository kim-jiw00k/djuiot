# reshape() 함수 사용
import numpy as np
a = np.arange(1,13)
print(a)
print()
b = a.reshape((3,4))
print(b)
print()
c = a.reshape((4,3))
print(c)
print()
d = a.reshape((-1,3))       #-1 은 자동으로 row를 맞춰주는 것
print(d)