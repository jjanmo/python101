x = 15
y = 25

print(f"x == y : {x == y}")  # False
print(f"x is y : {x is y}")  # False


x = ["orange", "banana", "apple"]
y = x

print(f"x == y : {x == y}")  # True
print(f"x is y : {x is y}")  # True


x = ["orange", "banana", "apple"]
y = ["orange", "banana", "apple"]

print(f"x == y : {x == y}")  # True → 다른 객체이여도 값(내용물)이 같기 때문에 True
print(f"x is y : {x is y}")  # False


"""
== 과 is 의 차이
- == : 값(객체라면 그 안의 내용물)이 같은지 비교
- is : 객체가 같은지 비교, id() 값이 같은지 비교, 같은 메모리 주소를 가리키는지 비교

vs

javascript에서의  == 과 === 의 차이
- == : 느슨한 동등 비교, 값을 비교하며, 필요하면 타입 변환을 통해 비교
 → 타입변환시 숫자로 변환 or 원시값으로 변환 후 비교
- === : 엄격한 동등 비교, 값과 타입을 모두 비교

✔️ 파이썬과 자바스크립트의 비교연산자 간에는 차이가 있음
"""

print("--------------------------------------------------")

a = 15
b = 25

print(f"결과1 > a == b : {a == b}")  # False
print(f"결과1 > a is b : {a is b}")  # False

print()

c = []
d = c
e = c + d

print(f"결과2 > c == d : {c == d}")  # True
print(f"결과2 > c is d : {c is d}")  # True
print(f"결과2 > c == e : {c == e}")  # True
print(
    f"결과2 > c is e : {c is e}"
)  # 중요 # False → c와 e는 같은 값을 가지지만, 다른 객체(다른 참조값을 가짐)이기 때문에 False

print()

print(f"c value, id : {c}, {hex(id(c))}")  # [], 0x104684980
print(f"d value, id : {d}, {hex(id(d))}")  # [], 0x104684980
print(f"c value, id : {e}, {hex(id(e))}")  # [], 0x1046ce740
