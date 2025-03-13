# 변수를 선언
example_list = ["요소 A","요소 B","요소 C"]

# 그냥 출력
print("# 단순 출력")
print(example_list)
print()

# enumerate() 함수를 적용하여 출력
print("# enumerate() 함수를 적용하여 출력")
print(enumerate(example_list))
print()

# list() 함수로 강제 변환하여 출력
print("# list() 함수로 강제 변환하여 출력")
print(list(enumerate(example_list)))
print()

# for 반복문과 enumerate() 함수 조합하여 사용
print("# 반복문과 조합하여 사용")
for i , value in enumerate(example_list):
    print(f"{i}번째 요소는 {value} 입니다.")