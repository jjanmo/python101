def solution(arr1, arr2):
    new_arr = arr1 + arr2
    new_arr.sort()

    return new_arr


print(solution([1, 3, 5], [2, 3, 6, 7, 9]))
