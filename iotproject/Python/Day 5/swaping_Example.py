def swap_func(first:int, second:int) -> tuple:
    (a,b) = (first, second)
    return (b, a)

(a, b) = (10, 20)
(a, b) = swap_func(a, b)
print(a)
print(b)