# flatten 함수 사용 평탄화 시키는 함수
import numpy as np

ary1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("원본")
print(ary1)
print()
print("flatten() 함수로 인한 평탄화")
ary2 = ary1.flatten()
print(ary2)
print()
# trancepose 전치 시키면 행 -> 열 , 열 -> 행 이 되어 버린다.
print("trancepose()함수 사용")
print(ary1.T)