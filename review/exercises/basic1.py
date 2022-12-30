# range
# a = range(10)  # 0 <= ~ < 10
# print(list(a), type(a))
# b = range(1, 10, 2)  # 1 <= ~ < 10, 스텝 2
# print(list(b))
# for i in b:
#     print(i)
#
# for i in range(10, 0, -1):  # 1씩 줄어드는 배열
#     print(i)

# for else
# for i in range(0, 10):
#     print(i)
#     if i > 10:
#         print('intermediate termination')
#         break
# else:
#     print('normal termination')


"""
반복문 문제
1) 1 ~ N 까지 홀수 출력하기
2) 1 ~ N 까지 합 출력하기
3) N의 약수 출력하기
"""


def print_odd(n):
    for i in range(1, n + 1):
        if i % 2 != 0:
            print(i)


# print_odd(10)


def print_sum(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i

    print(total)


# print_sum(10)


def print_divisor(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)

    print(result)


# print_divisor(12)

# 중첩 반복문(2중 for문)

# for i in range(5):
#     print(f'i=>{i} :', sep='', end=' ')
#     for j in range(5):
#         print('j:', j, sep='', end=' ')
#     print()

def print_star1():
    # sol1)
    # for i in range(5):
    #     for j in range(5):
    #         if i >= j:
    #             print('*', end=" ")
    #     print()
    # sol2)
    for i in range(5):
        for j in range(i + 1):
            print('*', end=" ")
        print()


# print_star1()


def print_star2():
    for i in range(5):
        for j in range(5 - i):
            print('*', end=" ")
        print()


print_star2()
