# 3장 PDF 86 page
import numpy as np

a = np.array([[1, 1, -1], [2, -1, 3], [1, 2, 1]], dtype='int32')
b = np.array([[0], [9], [8]], dtype='int32')
s = np.linalg.solve(a, b)
print(s)

det_a = np.linalg.det(a).round(2)

print(det_a)