# 1부터 20까지 홀수 * 10, 짝수는 그대로 리스트로 출력하세요.
# [10, 2, 30, 4, 50, 6, 70, 8, 90, 10, 110, 12, 130, 14, 150, 16, 170, 18, 190, 20]


def operate(num):
    if num % 2 == 1:
        return num * 10
    else:
        return num


list = list(map(operate, list(range(1, 21))))
print(list)
