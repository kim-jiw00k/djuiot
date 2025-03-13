for _ in range(10):     # 그냥 값을 가져오지 않고 돌리고 싶으면 _을 써야함 0 ~ 9
    print("Hello")

for i in range(100):    # 값을 가져올려면 i 를 써야함 0 ~ 99
    print(i + 1)

#range는 함수가 아닌 클래스 이다.

for _ in "Hello":
    print("Hello world")        # 시퀀셜 타입

for item in "Hello":
    print(f'값은 : {item}')

values = [1, 2, 3, 4, 5, 6]     # while은 무작위성 for 문은 순서성
for value in values:
    print(value)

print(values)

list_of_list = [[1, 2, 3],[4, 5, 6, 7], [8, 9]]

for i in list_of_list:      
    for j in i:
        print(j)