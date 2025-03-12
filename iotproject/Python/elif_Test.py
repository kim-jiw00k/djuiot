# 날짜 / 시간 기능
import datetime

# 현재 날짜 가져옴
# 쉽게 사용할 수 있게 월을 변수에 저장
now = datetime.datetime.now()
month1 = now.month

# 조건문으로 계절을 확인
if 3 <= month1 <= 5:
    print("현재는 봄 입니다.")
elif 6 <= month1 <= 8:
    print("현재는 여름 입니다.")
elif 9 <= month1 <= 11:
    print("현재는 겨울 입니다.")
else:
    print("현재는 겨울 입니다.")