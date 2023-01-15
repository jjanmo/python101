def solution(string):
    result = ''
    for char in string:
        if char.isdigit():  # isdecimal(0~9까지의 숫자만 숫자로 취급)  vs isdigit(0~9 +  2^2같은 숫자가 나올수 있는 값들 모두 숫자로 취급)
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


# 문자열의 특징을 사용하지않고 반복하면서 자리수 증가 로직(int를 사용하지 않는 풀이)
# res = res * 10 + n
# 결과값이 10을 곱함으로서 자리수를 증가시키는 로직
def solution2(string):
    result = 0
    for i in string:
        if i.isdecimal():
            result = result * 10 + int(i)
    print(result)


solution2('g0en2Ts8eSoft')  # 28
solution2('Akdj0Gk1djADG2SDGkdjf')  # 12
