# 문제이해가 어려운 문제!!
def solution(m, n):
    sum_dict = {}
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            sum_value = i + j
            if sum_value in sum_dict:
                sum_dict[sum_value] = sum_dict[sum_value] + 1
            else:
                sum_dict[sum_value] = 1

    max_key = max(sum_dict, key=sum_dict.get)
    max_value = sum_dict[max_key]

    result = []
    for key, value in sum_dict.items():
        if max_value == value:
            result.append(key)

    return result


print(solution(4, 6))
