# # function
# from typing import List, Any
#
#
# def print_coin():
#     for i in range(100):
#         print(i + 1, '비트코인')
#
#
# print_coin()
#
#
# # 215
# def print_with_smile(str):
#     print(str + ':D')
#
#
# print_with_smile('happy coding')
#
#
# # 217
# def print_upper_price(value):
#     print(value * 1.3)
#
#
# print_upper_price(2300)
#
#
# # 219
# def print_arithmetic_operation(num1, num2):
#     print(f'{num1} + {num2} = {num1 + num2}')
#     print(f'{num1} - {num2} = {num1 - num2}')
#     print(f'{num1} * {num2} = {num1 * num2}')
#     print(f'{num1} / {num2} = {num1 / num2}')
#
#
# print_arithmetic_operation(10, 12)
#
#
# def print_max(a, b, c):
#     if a >= b >= c:
#         print(a)
#     elif b >= b >= c:
#         print(b)
#     else:
#         print(c)
#
#
# print_max(10, 3, 44)


def print_reverse(string):
    print(string[::-1])


print(print_reverse('hello world'))


def print_score(scores):
    print(sum(scores) / len(scores))


print(print_score([70, 80, 100]))


def print_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(number)


print_even([1, 3, 2, 10, 12, 11, 15])


# def print_keys(info):
#     # 1)
#     # for key in info:
#     #     print(info[key])
#     # 2)
#     # for key in info.keys():
#     #     print(info[key])
#     # 3)
#     for value in info.values():
#         print(value)
#
#
# print_keys({"이름": "김말똥", "나이": 30, "성별": 0})


# my_dict = {"10/26": [100, 130, 100, 100],
#            "10/27": [10, 12, 10, 11]}
#
#
# def print_value_by_key(info, date):
#     # babo code --;
#     # for key, ohlc in info.items():
#     #     if key == date:
#     #         print(ohlc)
#     print(info[date])
#
#
# print_value_by_key(my_dict, "10/26")


# 226
# def print_5xn1(string):
#     for i, char in enumerate(string):
#         if i != 0 and (i + 1) % 5 == 0:
#             print(char)
#         else:
#             print(char, end="")
#
#
# def print_5xn2(string):
#     check = int(len(string)/5)
#     for i in range(check+1):
#         print(string[i*5:i*5+5])
#
#
# print_5xn1("아이엠어보이유알어걸니니")
# print(" ")
# print_5xn2("아이엠어보이유알어걸니니니")


# 227

def print_mxn(string, number):
    check = int(len(string) / number)
    for i in range(check + 1):
        print(string[i * number:i * number + number])


print_mxn("아이엠어보이유알어걸", 3)


# 228
def calc_monthly_salary(annual_salary):
    monthly_salary = int(annual_salary / 12)
    print(monthly_salary)


calc_monthly_salary(12000000)
calc_monthly_salary(13000000)


# 300
def add(a, b):
    print(a + b)


add(a=200, b=100)
add(b=100, a=200)  # 이렇게 인자를 바인딩하여 사용할 수 있음 / 순서대로 넣지않을 때는 바인딩 필요


# 332
def make_url(string):
    return f'www.{string}.com'


print(make_url("naver"))


def make_list(string):
    return list(string)  # split을 사용하지 않음 : 자바스크립트와 다름


print(make_list("abcd"))


def pickup_even(numbers):
    new_list = []
    for number in numbers:
        if number % 2 == 0:
            new_list.append(number)

    return new_list


print(pickup_even([3, 4, 5, 6, 7, 8]))


def convert_int(string_int):
    new_string = string_int.split(',')
    return int(''.join(new_string))


# replace(',','')

print(convert_int("1,234,567"))


