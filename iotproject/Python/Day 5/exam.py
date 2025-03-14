numbers = [1, 2, 3, 4, 5, 6]
print("::".join(map(str,numbers)))


number = list(range(1, 10+1))
print("# 홀수만 추출하기")
print(list(filter(lambda x:x % 2 == 1,number)))
print()
print("# 3이상 7 미만 추출하기")
print(list(filter(lambda x:3<=x<7,number)))
print()
print("# 제곱해서 50 미만 추출하기")
print(list(filter(lambda x:x ** 2 < 50,number)))
print()