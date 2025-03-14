# 랜덤한 숫자 만들기 위한 참조
import random
# 간단한 한글 리스트
hanguls = list("가나다라마바사아자파카타파하")
# 파일 쓰기 모드
with open("info.txt","w") as file:
    for i in range(1000):
# 랜덤한 값으로 변수 생성
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140,200)
        #텍스트 사용
        file.write(f"{name},{weight},{height}")