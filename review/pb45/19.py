# 각각의 a 는 어떤 값을 출력하는가?

a = 20


def test():
    a = 35
    return a


print("step1 : ", a)  # 20

a = 100

print("step2 : ", a)  # 100
print("step3 : ", test())  # 35


print("########")

b = 20


def test1():
    global b
    print(b)
    b = 35
    return b


print(b)  # 20

b = 100

print(b)  # 100
print(test1())  # 함수 내부 프린트 100 / 함수 리턴 35
print(b)  # 35
