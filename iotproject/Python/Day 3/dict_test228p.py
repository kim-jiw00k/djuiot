# 숫자는 무작위로 입력해도 상관 없음
numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}

for number in numbers:
    counter[number] = numbers.count(number)

print(counter)