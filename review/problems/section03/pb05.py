def solution(n, m, arr):
    total = 0
    start = 0
    count = 0
    for i in arr:
        total += i
        if total == m:
            count += 1
        elif total > m:
            while total > m:
                total -= arr[start]
                if total == m:
                    count += 1
                start += 1

    return count


print(solution(8, 3, [1, 2, 1, 3, 1, 1, 1, 2]))
print(solution(100, 100, [
    3, 3, 1, 4, 5, 2, 2, 5, 2, 1, 2, 2, 1, 1, 4, 1, 4, 3, 3, 5, 1, 5, 1, 3, 4, 5,
    4, 5, 2, 4, 2, 1, 1, 4, 2, 1, 5, 3, 1, 3, 1, 1, 1, 2, 4, 4, 5, 5, 5, 5, 3, 2,
    5, 5, 3, 2, 3, 4, 1, 3, 3, 4, 5, 1, 3, 1, 3, 2, 3, 1, 2, 3, 2, 5, 5, 4, 2, 3,
    1, 2, 3, 2, 4, 5, 2, 4, 4, 4, 4, 3, 1, 5, 2, 2, 1, 3, 2, 5, 4, 1,
]))