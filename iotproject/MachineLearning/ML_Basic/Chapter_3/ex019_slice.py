import numpy as np

ary2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9],
                  [0, 1, 2]])
print(ary2d[0][0])      # C언어 스러운 방식
print(ary2d[0, 0])      # numpy가 권장하는 방식,[0, 0]에서 앞이 axis=0,뒤가 axis=1 이다
print(ary2d[1:, 0:2])   # 이걸 더욱 선호함
print()

print("논리 인덱싱 나누기") # 브로드캐스팅이 일어남
ary2_2d = np.array([[1, 2, 3,4],[5, 6, 7, 8],[9, 10, 11, 12], [13, 14, 15, 16]])
print(ary2_2d % 2 == 0)
print(ary2_2d[ary2_2d % 2 == 0])# 참 인 것만 출력 하는 방식 3장 PDF 60 page 중요