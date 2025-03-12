# 딕셔너리 요소 추가

# 딕셔너리 선언
dict = {}

# 요소 추가 전 내용 출력
print("요소 추가 이전 : ", dict)

# 딕셔너리 요소 추가
dict["name"] = '새로운 이름'
dict['head'] = '새로운 정신'
dict['body'] = '새로운 몸'

# 출력
print('요소 추가 이후 : ',dict)

# 딕셔너리 요소 제거

# 딕셔너리 선언
dict_2 = {"name" : "7D 건조 망고",
          "type" : "당절임",
          }
# 요소 제거 전 출력
print("요소 제거 전 출력 : ", dict_2)

del dict_2 ["name"]
del dict_2 ["type"]

# 요소 제거 후 출력
print("요소 제거 후 출력", dict_2)