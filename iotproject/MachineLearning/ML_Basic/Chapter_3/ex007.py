from math import radians

import numpy as np

ary_1 = np.arange(1, 10)
print(ary_1)
print(ary_1.shape)
print(type(ary_1))
print()

ary_2 = np.arange(1, 10, 2)
print(ary_2)
print(ary_2.shape)
print(type(ary_2))
print()

ary_3 = np.linspace(0.0, 1.0, 100)
print(ary_3)
print(ary_3.size)
print()

ary_4 = np.logspace(1, 10, 10)
print(ary_4)
print()

ary_5 = np.log10(ary_4)
print(ary_5)
print()

# pdf 챕터 3 23 page 문제
t = np.linspace(0,np.pi,11)
print(np.sin(t))    # sin 함수
print(np.cos(t))    # cos 함수
print(np.tan(t))    # tan 함수
