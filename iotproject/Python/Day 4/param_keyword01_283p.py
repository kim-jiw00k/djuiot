def print_n_times(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
            pass
        print()
        pass
    pass

print_n_times("안녕하세요","즐거운","파이썬 프로그래밍",n=3)    #n=3 이게 키워드 매개변수