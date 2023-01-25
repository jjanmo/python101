# 슬라이싱으로 하면 인덱스가 계속 바뀌면서 더 복잡해짐.
# 잊어버릴때쯤 다시 풀기!!
def solution(locations):
    array = list(range(0, 21))

    for start, end in locations:
        diff = end - start
        for i in range((diff + 1) // 2):
            array[start + i], array[end - i] = array[end - i], array[start + i]

    return array[1:]


print(solution([
    [5, 10],
    [9, 13],
    [1, 2],
    [3, 4],
    [5, 6],
    [1, 2],
    [3, 4],
    [5, 6],
    [1, 20],
    [1, 20],
]))
print(solution([
    [7, 15],
    [7, 9],
    [1, 2],
    [3, 19],
    [1, 1],
    [1, 9],
    [2, 9],
    [5, 6],
    [1, 3],
    [1, 9],
]))
print(solution([
    [7, 15],
    [7, 9],
    [1, 2],
    [3, 19],
    [1, 1],
    [1, 9],
    [2, 9],
    [5, 6],
    [1, 3],
    [1, 9],
]))
print(solution([
    [13, 17],
    [2, 19],
    [1, 2],
    [3, 19],
    [1, 1],
    [1, 9],
    [11, 16],
    [5, 6],
    [1, 3],
    [1, 9],
]))
