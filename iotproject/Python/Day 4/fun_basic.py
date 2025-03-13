#def print_3_time():
#    for _ in range(3):
#        print("안녕하세요")

#print_3_time()

# 밑에 거가 조금 더 좋음
"""
def print_3_time(value) -> None:
    for _ in range(3):
        print("안녕하세요 " + str(value))
        value += 1
    return None
value = 1
print_3_time(value)
"""
def print_3_time(value1, value2 = 1):   #default parameter 는 뒤쪽에 써야한다. ex) value1 이 아닌 value2에 넣어야함
    for _ in range(3):
        print("안녕하세요" + str(value1) + "," + str(value2))

print_3_time(10)
