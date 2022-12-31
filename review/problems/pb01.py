def solution(n, k):
    """
    :param n: 숫자 n (n의 약수)
    :param k: 순서 k (k번째 순서)
    :return: n의 약수 중에서 k번째에 해당하는 수
    """

    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)

    return -1 if len(result) < k else result[k - 1]


print(solution(6, 3))  # 3
print(solution(8, 4))  # 8
print(solution(25, 5))  # -1
print(solution(1000, 12))  # 125
print(solution(7, 1))  # 1
