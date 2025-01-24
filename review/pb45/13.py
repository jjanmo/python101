# 아래와 같은 딕셔너리 구조에서 Value 값이 25 이상  필터링 후 출력하세요.
# 출력 결과 : {'b': 33, 'd': 26, 'f': 120}


d = {"a": 8, "b": 33, "c": 15, "d": 26, "e": 12, "f": 120}


# sol1
dict1 = {}
for key, value in d.items():
    if value >= 20:
        dict1[key] = value
print(dict1)

# sol2
filtered = filter(lambda t: t[1] >= 25, d.items())
# filtered = filter(lambda t: (lambda key, value: value >= 25)(*t), d.items()) # 위 코드를 unpacking 하는 방식으로 변경한 코드
print(dict(filtered))
