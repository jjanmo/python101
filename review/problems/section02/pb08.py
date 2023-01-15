def solution(numbers):
    result = []
    reversed_numbers = list(map(reverse, numbers))

    # 아래코드를 따로 루프를 돌 필요 없네...
    # reverse와 is_prime을 한번의 반복문으로 연산 가능!
    for number in reversed_numbers:
        if is_prime(number):
            result.append(number)

    return ' '.join(map(str, result))


def reverse(number):
    str_number = list(str(number))
    str_number.reverse()
    return int(''.join(str_number))


# 수학적 연산을 이용한 reverse
def reverse2(number):
    result = 0
    while number != 0:
        tmp = number % 10
        result = result * 10 + tmp  # 10을 곱해서 자리수는 높임
        number //= 10  # 10을 나눔으로서 자리수는 낮춤

    return result


# 좀 더 효율적인 코드를 위한 반복문 수정 : 딱 절반까지만 돌면 된!
def is_prime(number):
    if number == 1:
        return False

    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    else:
        return True


def checker(number):
    tmp = reverse(number)
    if is_prime(tmp):
        return tmp


def solution2(numbers):
    result = list(map(checker, numbers))
    for v in result:
        if v is not None:
            print(v, end=" ")
    print()


solution2([32, 55, 62, 3700, 250])

print(solution([32, 55, 62, 3700, 250]))  # 23 73
print(solution(
    [469, 84, 8851, 189, 69, 1210, 682, 57, 6217, 484, 8, 3590, 662, 36, 8275, 887, 17, 1254, 462, 67, 8969, 141, 70,
     5603, 958, 100, 3843]))  # 953 71 7 859
print(solution(
    [736, 89, 35, 19349, 287, 71, 719, 27200, 437, 82, 1399, 23763, 591, 8, 6793, 16256, 482, 14, 7725, 24830, 328, 60,
     2345, 4304, 348, 42, 6191, 8905, 168, 19, 4026, 19408, 897, 59, 9673, 15329, 857, 38, 2331, 6484, 469, 19, 2652,
     16738, 880, 87, 8479, 29157, 976, 59, 7196, 16479, 616, 50, 7979, 574, 486, 79, 898, 2654, 885, 53, 620, 24528,
     134, 32, 4443, 20954, 762, 77, 1775, 3390, 507, 25, 3271, 5823, 388, 47, 2727, 20194, 677, 90, 6107, 25330, 204,
     72, 9099, 20294, 241, 92, 6511, 22215, 121, 17, 6597, 5036, 685, 88, 2368, 1416]))
# 53 17 9931 41 823 80491 3769 83 83761 6917 5 97 431 23 1723 883 29 71
