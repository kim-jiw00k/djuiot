print("안녕"+"하세요")
# 문자열과 숫자 사이에는 사용할 수 없음
# print("안녕하세요"+1) << X
# print("안녕하세요"+"1") 아니면 print("안녕하세요"+ str(1))
print("")

#문자열 반복 연산자 : *
print("안녕하세요" * 3)
print("")

# 문자 선택 연산자 (인덱싱) : []
print("문자 선택 연산자에 대해 알아보자.")
str1 = "안녕하세요"
print(str1[0])  # 임시 객체
print(str1[1])
print(str1[2])
print(str1[3])
print(str1[4])
print("")

# 숫자를 0부터 셈 : 제로 인덱스
# 숫자를 1부터 셈 : 원 인덱스 ex)MATLAB
# 문자를 거꾸로 출력
print("문자를 뒤에서 부터 선택 해보자.")
print(str1[-1]) #요
print(str1[-2]) #세
print(str1[-3]) #하
print(str1[-4]) #녕
print(str1[-5]) #안
print("")

#slice 연산자
print(str1[1:4]) #for(int i = 0; i<4; ++i)랑 비슷한 소리
print(str1[0:2]) #안녕
print(str1[1:3]) #녕하
print(str1[2:4]) #하세
print(str1[0:5]) #안녕하세요
print(str1[0:-1])#안녕하세
print("")

#len() 함수 문자열의 길이 및 데이터의 길이를 구할때 사용
print(len(str1))
