# 변수로 사용할 수 없는 이름

a = 15
_b = 3.14
# 2c = int(77) # 변수로 사용할 수 없는 이름
_7d = float(5.14)

print(a, _b, _7d)


"""
파이썬에서 변수로 가능/불가능
- 키워드(예약어)를 사용불가
- 특수 문자는 언더 바(_)만 사용가능(*,$,% 등 불가)
- 숫자로 시작할 수 없음(js/ts도 마찬가지)
- 공백 불가
"""
