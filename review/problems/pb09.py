def solution(results):
    return max(list(map(get_reward2, results)))


def get_reward(numbers):
    numbers.sort(reverse=True)
    same_num = numbers[0]
    same_count = 0

    for num in numbers:
        if same_num == num:
            same_count += 1
        else:
            same_num = num

    if same_count == 3:
        return 10000 + same_num * 1000
    elif same_count == 2:
        return 1000 + same_num * 100
    else:
        return numbers[0] * 100


# get_reward에서 굳이 어렵게 풀 필요가 없었음...
def get_reward2(numbers):
    numbers.sort(reverse=True)
    a, b, c = numbers

    if a == b and b == c:
        return 10000 + a * 1000
    elif a == b or a == c:
        return 1000 + a * 100
    elif b == c:
        return 1000 + b * 100
    else:
        return a * 100


print(solution([
    [3, 3, 6], [2, 2, 2], [6, 2, 5]
]))
