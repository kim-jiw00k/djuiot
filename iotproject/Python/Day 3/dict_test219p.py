# 딕셔너리 선언
dict = {"name" : "7D 건조 망고",
        "type" : "당절임",
        "ingredient" : ["망고","설탕","메타중아황산나트륨","치자황색소"],
        "origin" : "필리핀",
}

# 출력
print("name : ",dict["name"])
print("type : ",dict["type"])
print("ingredient : ",dict["ingredient"])
#print("ingredient : ",dict["ingredient"][0]) 전자는 전체를 보여 주는것 후자는 0번째 만 보여주는 것
print("origin : ",dict["origin"])
print()

#값 변경
dict["name"] = "8D 건조 망고"
print("name : ",dict["name"])
