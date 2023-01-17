# O(nlog(n))
def solution1(arr1, arr2):
    new_arr = arr1 + arr2
    new_arr.sort()

    return new_arr


print(solution1([1, 3, 5], [2, 3, 6, 7, 9]))


# O(n)
def solution2(n, arr1, m, arr2):
    p1 = 0
    p2 = 0
    new_arr = []
    while p1 < n and p2 < m:
        if arr1[p1] < arr2[p2]:
            new_arr.append(arr1[p1])
            p1 += 1
        else:
            new_arr.append(arr2[p2])
            p2 += 1

    if p1 == n:
        new_arr += arr2[p2:]
    if p2 == m:
        new_arr += arr1[p1:]

    return new_arr


print(solution2(3, [1, 3, 5], 5, [2, 3, 6, 7, 9]))
