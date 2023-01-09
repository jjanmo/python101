def solution(results):
    return max(list(map(get_reward, results)))


def get_reward(numbers):
    numbers.sort(reverse=True)
    same_num = numbers[0]
    same_count = 0

    for num in numbers:
        if same_num == num:
            same_count += 1
        else:
            same_num = num
    print(same_count, same_num)

    if same_count == 3:
        return 10000 + same_num * 1000
    elif same_count == 2:
        return 1000 + same_num * 100
    else:
        return numbers[0] * 100


solution([
    [3, 3, 6], [2, 2, 2], [6, 2, 5]
])
