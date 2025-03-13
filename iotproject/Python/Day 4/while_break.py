# 변수 선언
i = 0

# 무한 반복
while True:
    # 반복 횟수 출력
    print(f"{i}번째 반복문 입니다.")
    i = i + 1
    #반복 종료
    input_text = input("> 종료하시겠습니까?(y) : ")
    if input_text in ["y","Y"]:
        print("반복을 종료 합니다.")
        break