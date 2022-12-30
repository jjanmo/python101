def operate(a, b):
    return a + b, a - b, a * b, a / b  # 여러 개 리턴 가능(튜플로서 리턴)


add, sub, mul, div = operate(10, 5)


# print(add, sub, mul, div)


def print_prime(n):
    for i in range(n + 1):
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        if count == 2:
            print(i)


# print_prime(10)  # 1 2 3  5  7


def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


for k in [12, 13, 7, 9, 19]:
    if is_prime(k):
        print(k, end=' ')
print()


# 람다함수 (익명함수, 람다표현식)
def plus_one(x):
    return x + 1


# lambda_plus_one = lambda x: x + 1

print(plus_one(10))
# print(lambda_plus_one(11))

a = [3, 4, 5]
print(list(map(plus_one, a)))
print(list(map(lambda x: x + 1, a)))  # plus_one이라는 함수를 람다함수로 한번에 표현 가능
