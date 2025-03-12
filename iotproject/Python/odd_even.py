input_value = input("숫자를 입력 : ")
last_digit = input_value[-1]
#last_digit = int(last_digit)
print(last_digit)

if last_digit in "02468":
    print("짝수")
else:
    print("홀수")

#if last_digit in "02468":
    print("짝수")
#if last_digit in "13579":
    print("홀수")

#if last_digit % 2 == 0:
#    print("짝수")
#else:
#    print("홀수")