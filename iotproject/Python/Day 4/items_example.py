dict_1 = {
    "key1" : "value1",
    "key2" : "value2",
    "key3" : "value3"
}

for (key, value) in dict_1.items():
    print(f"키는 : {key}, 값은 : {value}")

print(dict_1.items())   #dictionary overloading이 되어 있습니다. 값을 가져오는게 아닌 보여주기만 함