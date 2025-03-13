# 278page
def print_n_times(n, *values):  # *values 는 포인터가 아닌 많은 parameter가 온다는 뜻임 여러개 있을 땐 맨 뒤에 있어야 함
    # n번 반복
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times(3,1,2,3,4)