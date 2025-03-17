import numpy as np

a = np.arange(1,10)
a = a.reshape((3,3))
print(a)
print()

b = np.full((3,3),3)
print(b)
print()

print(a + b)
print()
print(a - b)
print()
print(a * b)
print()
print(a / b)
print()
print(a @ b)
print()
print(a ** 2)
print()