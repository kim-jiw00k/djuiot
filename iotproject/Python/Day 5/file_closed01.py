# try except 구문을 사용합니다.
try:
    #파일을 엽니다.
    file = open("info.txt","w")
    # 여러 가지 처리를 수행합니다.
    #파일을 닫음
    file.close()
except Exception as e:
    print(e)

print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed : ", file.closed)