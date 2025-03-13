# 리스트 선언
list_a = [1, 2, 3]
print(list_a)
print()

# 리스트 뒤에 새로운 리스트의 요소 모두 추가 extend()
print("# 리스트 뒤에 새로운 리스트의 요소 모두 추가 extend()")
list_a.extend([4,5,6])
print(list_a)
print()

# 리스트 뒤에 요소 추가
print("# 리스트 맨 뒤에 요소 추가 apeend(값)")
list_a.append(4)
list_a.append(5)
print(list_a)
print()

# 리스트 중간에 요소 추가
print("# 리스트 중간에 요소 추가 insert(위치,값)")
list_a.insert(0, 10)
print(list_a)
print()

# 리스트의 요소 하나 제거
list_b = [0,1,2,3,4,5]
print("# 리스트의 요소 하나 제거")
print(list_b)
print()

# 제거 방법[1] - del    슬라이스 연산자를 통해 범위를 지정해서 요소를 한꺼번에  제거 가능
del list_b[1]
print("del list_b[1] : ", list_b)
print()

# 제거 방법 [2] - pop()     index 2 를 빼라
list_b.pop(2)
print("pop(2) : ", list_b)
print()

# remove() 리스트에 요소 제거
print("# remove() 리스트에 요소 제거")
print()
list_c = [1,2,1,2]
print(list_c)
print()
list_c.remove(2)
print(list_c)
print()

# 모두 제거 하기 clear() 함수
print("#모두 제거 하기 clear() 함수")
print()
list_d = [0, 1, 2, 3, 4, 5]
print(list_d)
print()
list_d.clear()
print(list_d)
print()

# 특정값이 내부에 있는지 확인
print("# 특정값이 내부에 있는지 확인 in")
list_e = [273, 32, 103, 57, 52]
print(list_e)
print("list_e 안에 273 이 있는지 ? :",273 in list_e)
print("list_e 안에 99 가 있는지 ? :",99 in list_e)
print("list_e 안에 100 이 있는지 ? :",100 in list_e)
print("list_e 안에 52 가 있는지 ? :",52 in list_e)
print()
# 특정값이 내부에 없는지 확인
print("# 특정값이 내부에 없는지 확인 not in")
list_e = [273, 32, 103, 57, 52]
print(list_e)
print("list_e 안에 273 이 있는지 ? :",273 not in list_e)
print("list_e 안에 99 가 있는지 ? :",99 not in list_e)
print("list_e 안에 100 이 있는지 ? :",100 not in list_e)
print("list_e 안에 52 가 있는지 ? :",52 not in list_e)