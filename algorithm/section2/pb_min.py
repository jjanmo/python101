arr = [5, 3, 7, 9, 2, 5, 2, 6]


def get_min(array):
    min_value = arr[0]  # float('inf') 파이썬에서 가장 큰 값을 나타냄
    for v in array:
        if min_value > v:
            min_value = v
    return min_value


print(get_min(arr))
