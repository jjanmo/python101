def solution(N, M):
    sums = {}
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            tmp = i + j
            tmp_value = sums.get(tmp)
            if tmp_value is None:
                sums[tmp] = 0
            else:
                sums[tmp] = tmp_value + 1

    sums = list(sums.items())
    sums.sort(key=lambda _sum: _sum[1], reverse=True)

    result = []
    prev = -1
    for key, value in sums:
        if prev <= value:
            result.append(key)
            prev = value
        else:
            break

    return result


print(solution(4, 6))  # 5 6 7
print(solution(8, 8))  # 9
print(solution(6, 20))  # 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
