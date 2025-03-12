# 날짜/시간 기능 가져옴
import datetime

# 현재 날짜/시간구함
now = datetime.datetime.now()

#오전 구분
if now.hour < 12:
    print("현재 시각은 {}시로 오전 입니다!".format(now.hour))

#오후 구분
if now.hour >= 12:
    print("현재 시각은 {}시로 오후 입니다!".format(now.hour))