list_1 = [10, 20, 30, 40, 50, 60]
index = 1
for element in list_1:
    print(f"{index}번째 값은 : {element}")
    index += 1
    pass

print()

for index, element in enumerate(list_1):
    print(f"{index + 1}번째 값은 : {element}")