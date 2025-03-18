import numpy as np
ary_1 = np.array([1, 2, 3, 4])
print(ary_1.shape)  # 배열의 형상을 기술하며 m,n 형식의 튜플 형으로 나타냄 중요함
print(ary_1.ndim)   # 배열 축 혹은 차원의 개수를 나타냄
print(ary_1.dtype)  # 배열 원소의 자료형을 기술
print(ary_1.itemsize)   #배열 원소의 크기를 바이트 단위로 기술함. Ex)int32 자료형의 크기는 32/8=4 바이트가 됨
print(ary_1.size)       #배열 원소의 개수를 말하며 (m,n) 형상 배열의 size는 m*n 암
print(ary_1.data)   # 배열의 실제 원소를 포함하고 있는 버퍼