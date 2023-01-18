def solution(n, table):
    total = 0
    for row in table:
        cur = 0
        for i in row:
            cur += i
        if total < cur:
            total = cur

    for j in range(n):
        cur = 0
        for k in range(n):
            cur += table[k][j]
        if total < cur:
            total = cur

    d1 = 0
    d2 = 0
    for k in range(n):
        d1 += table[k][k]
        d2 += table[k][n - k - 1]
    if total < d1:
        total = d1
    if total < d2:
        total = d2

    return total


print(solution(5,
               [[10, 13, 10, 12, 15],
                [12, 39, 30, 23, 11],
                [11, 25, 50, 53, 15],
                [19, 27, 29, 37, 27],
                [19, 13, 30, 13, 19]]
               ))
