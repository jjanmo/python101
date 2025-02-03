d = {
    "group1": [
        {"name": "Park", "age": "32", "sex": "Male"},
        {"name": "Cho", "age": "44", "sex": "Female"},
        {"name": "Kang", "age": "39", "sex": "Female", "married": "No"},
    ],
    "group2": [
        {"name": "Kim", "age": "23", "sex": "Male", "married": "Yes"},
        {"name": "Lee", "age": "37", "sex": "Male", "married": "No"},
    ],
    "type": {
        "a": "employee",
        "b": "officer",
        "c": "director",
        "d": "manager",
        "e": "service provider",
    },
}

# 출력결과 : Name : Kim, Age : 23, Type : officer


kim = d.get("group2")[0]
name = kim["name"]
age = kim["age"]
type = d.get("type")["b"]
print(f"Name : {name}, Age : {age}, Type : {type}")


# 참고
# 파이썬의 딕셔너리과 자바스크립트의 객체는 구조적으로 같지만, 값의 접근 방법이 다르다.
# 딕셔너리 : []를 통한 접근, get(key)를 통한 접근
# get(key)의 경우, 키가 없을 경우 None 리턴, [] 의 경우 key가 없으면 에러를 리턴 → get을 사용하는 것이 안전하다!
# 자스의 객체는 dot notation 가능, 딕셔너리는 불가능!! → 가장 어메이징한 부분!
# dot notation을 사용하고 싶다면, 클래스를 만들어서 사용하면됨(일종의 data class)
