def solution(string):
    result = ''
    for char in string:
        if char.isdigit():
            result += char
    result = int(result)

    count = 0
    for i in range(1, result + 1):
        if result % i == 0:
            count += 1

    return result, count


print(solution('g0en2Ts8eSoft'))  # 28 6
print(solution('Akdj0Gk1djADG2SDGkdjf'))  # 12 6
print(solution('Akdj0Gk1dgdgdAGSGAG3DGGA45GAGADGDGdjADG2SDGkdj0f'))  # 134520 64
