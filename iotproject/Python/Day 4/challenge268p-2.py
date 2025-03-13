dna = input("염기 서열을 입력해주세요 : ")
counter = {}

for i in dna:
    counter[i] = dna.count(i)

# 각 염기 개수 출력
for dna_1,dna_2 in counter.items():     #counter 에서 키 와 값을 가져옴
    print(f"{dna_1}의 개수는 : {dna_2}")