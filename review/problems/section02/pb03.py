def solution1(numbers, order):
    s = list(set(numbers))

    new_numbers = set()
    for i, v1 in enumerate(s):
        for j, v2 in enumerate(s[i + 1:]):
            for k, v3 in enumerate(s[j + 1:]):
                tmp = v1 + v2 + v3
                new_numbers.add(tmp)

    res = list(new_numbers)
    res.sort(reverse=True)

    return res[order - 1]


"""
solution1이 오류 풀이인 이유
1) 문제 이해!
주어진 배에서는 중복이 허용된다. 단, 더해진 값에서 중복을 없애야한다,

2) 슬라이싱과 인덱스
배열을 슬라이싱하게되면 인덱스가 초기화된다. 
현재 문제에서는 기존의 인덱스를 계속적으로 유지해야함!
"""


def solution2(numbers, order):
    n = len(numbers)

    result = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                tmp = numbers[i] + numbers[j] + numbers[k]
                result.add(tmp)

    result = list(result)
    result.sort(reverse=True)

    return result[order - 1]


print(solution2([13, 15, 34, 23, 45, 65, 33, 11, 26, 42], 3))  # 143
print(solution2(
    [31, 40, 40, 49, 44, 53, 41, 25, 35, 53, 28, 36, 50, 38, 27, 23, 50, 42, 51, 20, 37, 48, 22, 37, 23, 42, 23, 39, 28,
     30, 31, 18, 24, 41, 48, 40, 21, 25, 25, 28, 24, 41, 49, 30, 36, 35, 15, 52, 36, 17, 49, 26, 43, 44, 43, 37, 30, 41,
     35, 20, 28, 25, 51, 16, 45, 15, 54, 54, 17, 40, 47, 27, 42, 22, 54, 47, 29, 29, 36, 29, 53, 42, 49, 42, 49, 16, 44,
     36, 30, 45], 30))  # 133
print(solution2(
    [38, 46, 54, 33, 34, 23, 48, 50, 23, 26, 46, 47, 25, 48, 35, 48, 32, 30, 50, 28, 39, 34, 24, 28, 26, 53, 18, 24, 52,
     41, 41, 33, 23, 52, 27, 22, 45, 30, 52, 19, 40, 48, 45, 23, 21, 45, 19, 20, 38, 21, 19, 21, 31, 40, 53, 27, 49, 48,
     30, 32], 20))  # 141
