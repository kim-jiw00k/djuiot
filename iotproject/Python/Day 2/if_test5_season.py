# 날짜/시간 기능 가져옴
import datetime

# 현재 날짜/시간구함
now = datetime.datetime.now()

#봄 구분
if 3 <= now.month <= 5 :
    print("이번 달은 {}월로 봄 입니다.".format(now.month))
#여름 구분
if 6 <= now.month <= 8 :
    print("이번 달은 {}월로 여름 입니다.".format(now.month))

# 가을 구분
if 9 <= now.month <= 11:
    print("이번 달은 {}월로 가을 입니다.".format(now.month))

# 겨울 구분
if now.month == 12 or 1 <= now.month <= 2  :
    print("이번 달은 {}월로 겨울 입니다.".format(now.month))