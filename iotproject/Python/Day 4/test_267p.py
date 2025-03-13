# 1~100 사이에 있는 숫자 중 2 진수로 변환 했을 때 0이 하나만 포함된 숫자를 찾고, 그 숫자들의 합을 구하는 코드를 만드시오.

# 리스트 내표를 사용해본 코드
output = [num for num in range(1,101) if "{:b}".format(num).count("0") == 1]


for i in output:
    print("{} : {}".format(i, "{:b}".format(i)))
    pass
print("합계 : ", sum(output))