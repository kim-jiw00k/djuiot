# 1 부터 100까지의 숫자가 있는데 두 숫자를 곱했을 때 최대치가 되는 경우는 어떤 숫자인지 찾으시오
max_value = 0
a = 0
b = 0

for i in range(100):
    j = 100 - i
#최댓값 구하기
    a = j
    b = i
    max_value = a * b
    max_value



print(f"최대가 되는 경우 : {a} * {b} = {max_value}")