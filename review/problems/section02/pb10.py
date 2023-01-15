def solution(result):
    score = 0
    count = 0
    for v in result:
        if v == 0:
            count = 0
        else:
            count += 1
            score += count
    return score


print(solution([1, 0, 1, 1, 1, 0, 0, 1, 1, 0]))
