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


# for문 통합
def solution2(n, table):
    total = 0
    for i in range(n):
        sum1 = sum2 = 0
        for j in range(n):
            sum1 += table[i][j]
            sum2 += table[j][i]
        if sum1 > total:
            total = sum1
        if sum2 > total:
            total = sum2

    sum1 = sum2 = 0
    for k in range(n):
        sum1 += table[k][k]
        sum2 += table[k][n - k - 1]
    if total < sum1:
        total = sum1
    if total < sum2:
        total = sum2

    return total


print(solution2(5,
                [[10, 13, 10, 12, 15],
                 [12, 39, 30, 23, 11],
                 [11, 25, 50, 53, 15],
                 [19, 27, 29, 37, 27],
                 [19, 13, 30, 13, 19]]
                ))
