#flip 함수 사용
import numpy as np

c = np.array([[1, 2, 3], [4, 5, 6]])
print("원본")
print(c)
print()
print("axis 가 1 일때 좌우 반전")
print(np.flip(c,axis=1))
print()
print("axis 가 0 일때 상하 반전")
print(np.flip(c,axis=0))
print()
print("원점 반전")
a = np.flip(c, axis=0)
b = np.flip(a, axis=1)
print(b)