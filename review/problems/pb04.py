import sys


def solution(numbers):
    total = 0
    for v in numbers:
        total += v

    avg = round(total / len(numbers))

    diff = sys.maxsize
    score = 0
    order = 0
    for i, v in enumerate(numbers):
        _diff = abs(v - avg)
        # print(_diff, diff, score, v)
        if _diff < diff:
            diff = _diff
            score = v
            order = i
        elif _diff == diff and score < v:
            score = v
            order = i
    return avg, order + 1


print(solution([45, 73, 66, 87, 92, 67, 75, 79, 75, 80]))  # 74 7
print(solution(
    [25, 60, 17, 60, 11, 15, 27, 42, 39, 31, 25, 36, 32, 25, 17, 45, 67, 89, 24, 65, 13, 34, 17, 6, 11, 15, 27, 42, 39,
     31, 25, 36, 32, 25, 17, 45, 67, 89, 24, 65, 13, 34, 17, 6, 11, 15, 27, 42, 39, 31, 25, 36, 32, 25, 17, 45, 67, 89,
     24, 65
     ]))  # 35 12
print(solution([1, 2, 3, 4, 5]))  # 3 3
