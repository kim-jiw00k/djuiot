import numpy as np
a = np.random.randint(150, 191, size= 10)
print("랜덤값 150부터 191 10개")
print(a)
print()

#randn 은 normalization 정규화

rnd = np.random.randn(5) * 10 + 165 #평균값이 165, 표준편차가 10인 값
print("평균값이 165, 표준편차가 10 인 값")
print(rnd)
print()

print("int형으로 표현")  # 원본을 바꾸지 않음
b = rnd.astype(int)
print(b)
print()

print("씨드 값을 가짐")   # 소수점 2째 까지 만들려면 round를 써야함 pdf 3장 52~53
np.random.seed(2025)
random_num1 = np.round(np.random.randn(3,4) * 10 + 165, 2)
random_num2 = np.random.normal(loc = 165, scale = 10, size = (3,4)).round(2)
print(random_num1)
print()
print(random_num2)
print()

print("shuffle() 함수 사용 랜덤 셔플")
a = np.arange(10)
np.random.shuffle(a)
print(a)
