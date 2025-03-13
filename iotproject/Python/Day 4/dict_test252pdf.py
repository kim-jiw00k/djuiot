limit = 1000

i = 1

# sum은 파이썬 내부에서 사용하는 식별자로 sum_value라는 변수를 사용

sum_value = 0

while sum_value < 1000:
    i += 1
    sum_value += i

print(f"{i - 1}를 더할 때 {limit}을 넘으며 그때의 값은 {sum_value}입니다.")