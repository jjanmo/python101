import json

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

# 1
json_obj = json.dumps(d, indent=8)
print(json_obj)

# 2
# "w" : 기존에 파일이 있으면 내용을 덮어씀. 없으면 새 파일을 자동으로 생성
# open의 리턴값을 파일 객체이기 때문에 그것을 out이라는 변수로 말할겠다는 의미
with open("./32.json", "w") as out:
    json.dump(d, out)


"""
json 내장 패키지 
- json.dump(obj, file) > JSON 데이터를 파일로 저장
- json.dumps(obj, indent) > JSON 데이터를 문자열로 반환 

"""
