fun1 = lambda x : x**2
print(fun1(10))

def power(x):
    return x ** 2           #Non Linear 비선형을 사용
x = [0, 1, 2, 3, 4, 5]

def linear_system(x):
    return 2 * x + 1        #Linear 선형을 사용

fx = map(power, x)
print(fx)
for item in fx:
    print(item, end="\t")

print()

linear_out = map(linear_system, x)
for item in linear_out:
    print(item, end="\t")

print("\r\n")
result = map(fun1, x)
print(result)
for item in result:
    print(item, end="\t")