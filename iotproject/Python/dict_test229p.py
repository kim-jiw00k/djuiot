# 딕셔너리 선언
character = { "name" : "기사",
              "level" : 12,
              "items" : {"sword" : "불꽃의 검",
                         "armor" : "풀 플레이트"},
              "skill" : ["베기","세게 베기","아주 세게 베기"]

}

for key in character:
    if type(character[key]) is list:
        for item in character[key]:
            print(f"{key} : {item}")
    elif type(character[key]) is dict:
        for item in character[key]:
            print(f"{item} : {character[key][item]}")
    else:
        print(f"{key} : {character[key]}")