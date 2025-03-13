list_a = [1,2,3,4,1,2,3,1,4,2,1,3]
counter = {}

for number in list_a:
    counter[number] = list_a.count(number)

print(counter)

