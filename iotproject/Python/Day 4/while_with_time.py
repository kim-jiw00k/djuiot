import time
#start_time = time.time()
#print(start_time)
#time.sleep(2)
#end_time = time.time()
#print(end_time)
#print(f"프로그램 로딩 시간 : {end_time - start_time}")

# 변수 선언
number = 0

# 5 초동안 반복
target_tick = time.time() + 5
while time.time() < target_tick:
    number += 1
    pass
# 출력
print(f"5초 동안 {number}번 반복 했습니다.")