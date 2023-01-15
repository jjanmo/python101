def solution(numbers, start, end, k):
    """
    :param numbers: 숫자 배열
    :param start: 시작 지점
    :param end: 종료 지점
    :param k: k번째
    :return: 숫자 배열에서 시작 배열 ~ 종료 시점에 해당하는 배열을 오름차순한 후 k번째 수
    """

    new_numbers = numbers[start - 1:end]
    new_numbers.sort()
    return -1 if len(new_numbers) < k else new_numbers[k - 1]


print(solution([5, 2, 7, 3, 8, 9], 2, 5, 3))  # 7
print(solution(
    [4, 15, 8, 16, 6, 6, 17, 3, 10, 11, 18, 7, 14, 7, 15],
    3,
    10,
    3
))  # 6
