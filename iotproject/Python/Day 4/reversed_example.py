numbers = list(range(1, 6))
print(numbers)

print(reversed(numbers))
print(numbers)

for item in reversed(numbers):
    print(item, end=", ")
    pass
print()
print(numbers[::-1])        # extended slicing 확장된 슬라이스 라고 함
print(numbers)

reversed_numbers = numbers[::-1]
print(reversed_numbers)

#reversed_numbers = reversed(numbers)