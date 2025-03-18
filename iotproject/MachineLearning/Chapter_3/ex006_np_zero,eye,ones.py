import numpy as np
pixel1 = np.zeros(shape = (2, 2)) + 255
print(pixel1)
print()

pixel2 = np.ones(shape = (2, 2)) * 255
print(pixel2)
print()

pixel3 = np.full(shape = (2, 2), fill_value = 255)
print(pixel3)
print()

pixel4 = np.eye(N = 5)
print(pixel4)
print()

# pdf 챕터 3 15 page 문제
pixel5 = np.eye(N = 4) * 10
print(pixel5)