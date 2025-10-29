# json to dictionary

import json

json_string = """
  {
    "group1": [
      { "name": "Park", "age": "32", "sex": "Male" },
      { "name": "Cho", "age": "44", "sex": "Female" },
      { "name": "Kang", "age": "39", "sex": "Female", "married": "No" }
    ],
    "group2": [
      { "name": "Kim", "age": "23", "sex": "Male", "married": "Yes" },
      { "name": "Lee", "age": "37", "sex": "Male", "married": "No" }
    ],
    "type": { "a": "employee", "b": "officer", "c": "director", "d": "manager", "e": "service provider" }
  }
"""
# 1번
dict = json.loads(json_string)
print(f"1번 {dict}")

# json.load() vs json.loads()
# json.load(file) : 파일 객체를 인자로 전달
# json.loads(string) : 인자로 문자열을 받음, 존재하는 데이터를 파싱할 때 사용


# 2번
with open("./32.json", "r") as f:
    # json = f.read()
    json = json.load(f)

print(f"2번 {json}")
