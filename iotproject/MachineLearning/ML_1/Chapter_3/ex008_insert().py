import numpy as np
# 1차원 배열
ary1 = np.array([1, 3, 4])
ary2 = np.insert(ary1,1,2)

print(ary2)
print()
# 2차원 배열 pdf 3장 26page 잘 보기 axis 방향 0은 세로방향으로 움직이며 가로로 들어감 1은 가로 방향으로 움직이며 세로 방향으로 들어감
print("axis 가 0 일때")
ary3 = np.array([[1, 1], [2, 2], [3, 3]])
ary4 = np.insert(ary3, 1, 4, axis=0)
print(ary4)
print()
print("axis 가 1 일때")
ary5 = np.array([[1, 1], [2, 2], [3, 3]])
ary6 = np.insert(ary5, 1, 4, axis=1)
print(ary6)