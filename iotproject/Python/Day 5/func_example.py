# f(x) = 2x + 1
def f_1(x):
    return 2 * x +1
print(f_1(10))


# f(x) = x**2 + 2x + 1
def f_2(x):
    return x**2 + 2 * x + 1
print(f_2(10))

def mul(*values):
    value = 1
    for i in values:
        value = value * i
    return value

print(mul(5, 7, 9, 10))