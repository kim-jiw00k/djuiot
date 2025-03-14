def tuple_fun():
    (a, b, c) = (10, 20, 30)
    return (a, b, c)

(A, B, C) = tuple_fun()
tuple1 = tuple_fun()
print(A)
print(B)
print(C)
print(tuple1[0])