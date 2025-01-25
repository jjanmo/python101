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


print(add(10, 20, 30))  # 위치 인자
print(
    add(b=30, c=40, a=20)
)  # 파이썬만의 특징 : 함수 호출 시 키워드 인자(key=value) 문법으로 사용할 수 있어서 순서에 관계없이 인자를 넣을 수 있다. → 키워드 인자
print(add(30, 40, 20))

# 상황 : a인자로 특정값을 지정해서 넣고 싶다면,,,
# print(add(a=30, 40, 50)) # 에러 : 위치 인자 뒤에 키워드 인자가 와야함
# print(add(40, 50, a=30)) # 에러 : 이미 a 인자로서 40이 위치인자가 들어갔는데, 키워드 인자를 a로 사용하였기때문에 오류
# 이런 경우는 인자를 넘기는 방식이 조정되어야함!!(문법적으로 오류)


# 참고
# https://levelup.gitconnected.com/5-types-of-arguments-in-python-function-definition-e0e2a2cafd29


def sum(*args):
    print(args, type(args))  # 기본적으로  *args로 가변 위치 인자를 받으면 "튜플"로 처리
    total = 0
    for i in args:
        total += i
    return total


print(sum(10))
print(sum(10, 20))
