import numpy as np

a = np.array([1, 2, 3])
b = np.array([[4, 5, 6], [7, 8, 9]])
c = np.append(a, b)
print(c)

# 2차원 배열로 만들어서 출력 하고 싶다면

d = np.append([a],b,0)
print(d)