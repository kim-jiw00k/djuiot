numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

print("# 홀수 짝수 구하기")
for i in numbers:
    if i % 2 == 0:
        print("{}는 짝수 입니다.".format(i))
    else:
        print("{}는 홀수 입니다.".format(i))

print()

j = str(numbers)
print("# 자릿수 구하기")
for j in numbers:
    if 10 > j >= 1:
        print("{} 는 1 자릿수 입니다.".format(j))
    elif 100 > j >= 10:
        print("{} 는 2 자릿수 입니다.".format(j))
    else:
        print("{} 는 3 자릿수 입니다.".format(j))

# 밑에사 파이썬 식으로 만든 것
"""
for number in numbers:
    convert_to_number = str(number)
    if convert_to_number[-1] in "02468":
        print(f'{convert_to_number}는 짝수 입니다.')
    else:
        print(f'{convert_to_number}는 홀수 입니다.')

for number in numbers:
    convert_to_number = str(number)
    print(f"{convert_to_number}는 {len(convert_to_number)} 자릿수 이다.")

"""