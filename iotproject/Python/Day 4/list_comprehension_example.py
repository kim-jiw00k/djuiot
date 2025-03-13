result = []
for i in range(0,20,2):
    result.append(i * i)
    pass
print(result)

result_2 = [i * i for i in range(0,20,2)]
print(result_2)

result_3 = [i * i for i in range(0,20) if i % 2 == 0]
print(result_3)