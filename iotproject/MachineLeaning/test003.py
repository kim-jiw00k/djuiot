import numpy as np

ary1 = np.array([[35, 24, 55], [69, 19, 9], [4, 1, 11]])

ary1.sort(1)
print(np.flip(ary1,1))

print()

ary2 = np.array([[35, 24, 55], [69, 19, 9], [4, 1, 11]])
ary2.sort(0)
print(ary2)