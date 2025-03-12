#날짜 / 시간 과 관련된 기능을 가져옴
import datetime

# 현재 날짜 / 시간을 구함
now = datetime.datetime.now()

#출력
#1
#print(now)
#print(type(now))
#2
#print(now.year, "년")
#print(now.month, "월")
#print(now.day, "일")
#print(now.hour, "시")
#print(now.minute, "분")
#print(now.second, "초")
#3
print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
))