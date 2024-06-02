arr = [5, 3, 7, 9, 2, 5, 2, 6]


def get_min(array):
    min_value = arr[0]  # float('inf') 파이썬에서 가장 큰 값을 나타냄
    for v in array:
        if min_value > v:
            min_value = v
    return min_value


print(get_min(arr))


def get_min1(array):
    min_value = arr[0]
    for i in range(1, len(array)):
        if min_value > array[i]:
            min_value = array[i]
    return min_value


print(get_min1(arr))