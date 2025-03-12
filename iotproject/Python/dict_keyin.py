# 딕셔너리 내부에 키가 있는지 확인하기

# 딕셔너리 선언
dict_1 = {"name" : "7D 건조 망고",
        "type" : "당절임",
        "ingredient" : ["망고","설탕","메타중아환산나트륨","치자황색소"],
        "origin" : "필리핀"
        }

# 사용자로부터 입력
key = input(" > 접근하고자 하는 키 : ")

# 출력
if key in dict_1:
    print(dict_1[key])
else:
    print("존재하지 않는 키에 접근하고 있습니다.")