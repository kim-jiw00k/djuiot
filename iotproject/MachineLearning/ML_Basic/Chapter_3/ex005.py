import numpy as np

list1 = [10, 20, 30]
value1 = 3
print(list1 * value1)

ary1 = np.array([10, 20, 30])
print(value1 * ary1)        # value1가 [3, 3, 3]이 되는데 이걸 브로드캐스팅 이라고 한다.
ary2 = np.array([3, 3, 3])
print(ary2 * ary1)