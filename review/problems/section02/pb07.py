# 아래 풀이는 큰 숫자는 구하지 못함.
# → 2중 반복문을 안돌고 혹은 적게 돌고 해결하는 방법을 찾아야함 : by 에라토스테니스 체
def solution(n):
    numbers = list(range(2, n + 1))
    for v in numbers:
        for k in range(v + 1, n + 1):
            if k % v == 0 and k in numbers:
                numbers.remove(k)

    return len(numbers)


# print(solution(20))  # 8
# print(solution(100))  # 25

# print(solution(150000))  # 13848
# print(solution(90000))  # 8713


def updated_solution(n):
    # prime = [0 for i in range(n + 1)]
    prime = [0] * n + 1  # 이런 방법으로도 0을 기본값으로 가진 리스트를 만들 수 있음 😅
    prime[0] = 1
    prime[1] = 1

    count = 0
    # prime의 index를 가지고 반복문을 도는 것!
    for i in range(n + 1):
        if prime[i] == 0:
            count += 1
            for j in range(i, n + 1, i):
                prime[j] = 1

    return count


print(updated_solution(20))  # 8
print(updated_solution(100))  # 25
print(updated_solution(1000))  # 168
print(updated_solution(150000))  # 13848
print(updated_solution(90000))  # 8713
