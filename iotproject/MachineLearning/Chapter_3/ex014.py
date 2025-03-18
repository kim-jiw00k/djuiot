import numpy as np

ary1 = np.array([[35, 24, 55], [69, 19, 9], [4, 1, 11]])
print("원본")
print(ary1)
print()

print("axis 1")
ary1.sort(axis=1)
print(ary1)
print()

ary2 = np.array([[35, 24, 55], [69, 19, 9], [4, 1, 11]])
print("axis 0")
ary2.sort(axis=0)
print(ary2)