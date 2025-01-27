def input_average(count):
    total = 0
    for _ in range(count):
        number = int(input())
        total += number

    return total / count


# print(input_average(3))


# 3개를 한번에 받는 방법

# sol1
a, b, c = input("숫자와 숫자 사이에 공백을 입력").split(" ")
print(a, b, c)
print((int(a) + int(b) + int(c)) / 3)

# sol2
l = list(map(int, input("숫자와 숫자 사이에 공백을 입력").split(" ")))
print(sum(l) / len(l))
