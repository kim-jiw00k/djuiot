import numpy as np

print("axis 별로 더하기")
print()
arr = np.array([[1, 2, 3, 4, 5],
                [1, 2, 3, 4, 5],
                [1, 2, 3, 4, 5],
                [1, 2, 3, 4, 5],
                [1, 2, 3, 4, 5]
                ])
print("*axis 0 으로 더하면*")
print(np.sum(arr, axis = 0))
print("**axis 1 로 더하면**")
print(np.sum(arr, axis = 1))
print("***axis 0,1 둘 다 더하면***")
print(np.sum(arr, axis= (0,1)))
print()

print("선형 방정식을 풀어보자")
a = np.array([[1, 2], [1, -3]])
b = np.array([6, 1])
s = np.linalg.solve(a, b)
print(s)
print()

print("3x3 행렬 선형 방정식을 풀어 보자")
c = np.array([[2, 1], [4, 5]])
det_c = np.linalg.det(c)
d = np.array([[1, 2], [3, -6]])
det_d = np.linalg.det(d)
print(det_c,det_d)