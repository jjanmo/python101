# 아래 풀이는 큰 숫자는 구하지 못함.
# → 2중 반복문을 안돌고 혹은 적게 돌고 해결하는 방법을 찾아야함
def solution(n):
    numbers = list(range(2, n + 1))
    for v in numbers:
        for k in range(v + 1, n + 1):
            if k % v == 0 and k in numbers:
                numbers.remove(k)

    return len(numbers)


print(solution(20))  # 8
# print(solution(150000))  # 13848
# print(solution(90000))  # 8713
