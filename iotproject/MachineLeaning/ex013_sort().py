# sort() 함수 사용 정렬
import numpy as np
ary1 = np.array([35, 24, 55, 69, 19, 99])
ary2 = ary1.sort()      # sort() 함수는 원본 수정
# 오름차순
print(ary1)             # 그래서 ary2 가 아닌 ary1 을 출력 해야함 ary2 는 None 비어 있음
# 내림차순
print(ary1[::-1])