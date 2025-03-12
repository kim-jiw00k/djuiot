# 딕셔너리 선언  get() 함수는 존재하지 않는 키에 접근할 경우 KeyError를 발생시키지 않고 None 을 출력함
dict_2 = {"name" : "7D 건조 망고",
        "type" : "당절임",
        "ingredient" : ["망고","설탕","메타중아환산나트륨","치자황색소"],
        "origin" : "필리핀"
        }

# 존재하지 않는 키에 접근
value = dict_2.get("존재하지 않는 키")
print("값 : ", value)

#None 확인 방법
if value == None:
    print("존재하지 않는 키에 접근 했었습니다.")
    pass

print()

# for in 같이 사용하는 법
dict_3 = {"name" : "7D 건조 망고",
        "type" : "당절임",
        "ingredient" : ["망고","설탕","메타중아환산나트륨","치자황색소"],
        "origin" : "필리핀"
        }

#for 반복문을 사용
for key in dict_3:
    #출력
    print(key,":", dict_3[key])