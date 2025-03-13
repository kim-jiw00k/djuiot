dna = input("염기 서열을 입력해주세요 : ")
counter = {}

for i in dna:
    counter[i] = dna.count(i)
