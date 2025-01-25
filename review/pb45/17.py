# 기본값이 있는 인자는 기본값이 없는 인자보다 앞에 있어야함!
def greet(
    name,
    msg="Good morning!",
):
    return "Hi! " + name + ", " + msg


# 실행
print(greet("Kim"))
print(greet("Park", "How do you do?"))


def add(a, b, c):
    print(f"a={a},b={b},c={c}")
    return a + b + c


print(add(10, 20, 30))
print(
    add(b=30, c=40, a=20)
)  # 파이썬만의 특징 : 함수 호출 시 키워드 인자(key=value) 문법으로 사용할 수 있어서 순서에 관계없이 인자를 넣을 수 있다.
print(add(30, 40, 20))
