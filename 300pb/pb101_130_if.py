# str = input()
# if str == "안녕하세요":
#     print(str * 2)


# num1 = input()
# print(int(num1) + 10)

# num2 = input()
# if (int(num2) % 2) == 0:
#     print("짝수")
# else:
#     print("홀수")

# num3 = input()
# result = int(num3) + 20
# if result > 255:
#     print(255)
# else:
#     print(result)


# fruit = ["사과", "포도", "홍시"]
# f = input()
# if f in fruit:
#     print("정답입니다.")
# else:
#     print("오답입니다.")

# fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
# keys = fruit.keys()
# season = input()
# if season in keys:
#     print("정답입니다.")
# else:
#     print("오답입니다.")

# char = input()
# if char.isupper():
#     print(char.lower())
# else:
#     print(char.upper())

# score = int(input())
# if 100 >= score > 80:
#     print("A")
# elif 80 >= score > 60:
#     print("B")
# elif 60 >= score > 40:
#     print("C")
# elif 40 >= score > 20:
#     print("D")
# else:
#     print("E")


# value = input().split(" ")
# print(value)

# rate = {"달러": 1167, "엔": 1268, "유로": 1268, "위안": 171}
# # 1)
# # print(float(rate[value[1]] * int(value[0])), "원")

# # 2)
# def getCurrency(str):
#     return rate.get(str, 0)

# print(getCurrency(value[1]) * float(value[0]))


# 1)
# values = input().split() # 아무것도 안넣으면 공백 기준으로 자름
# list = []
# for value in values:
#     list.append(int(value))

# print(max(list))

# 2)
# values = list(map(int, input().split()))
# # map(a,b) : a는 함수 / b는 리스트
# # -> b를 지정된 함수a로 처리하여 map 객체로 반환
# print(max(values))


# 125
# phone = input().split("-")
# first = phone[0]
# if first == "011":
#     print("당신은 SKT 사용자입니다")
# elif first == "016":
#     print("당신은 KT 사용자입니다")
# elif first == "019":
#     print("당신은 LGU 사용자입니다")
# elif first == "010":
#     print("알수없음")


# 126
# third = input()[2]

# if third == "0" or third == "1" or third == "2":
#     print("강북구")
# elif third == "3" or third == "4" or third == "5":
#     print("도봉구")
# else:
#     print("노원구")

# zip = input()[:3]
# if zip in ["010", "011", "012"]:
#     print("강북구")
# elif zip in ["013", "014", "015"]:
#     print("도봉구")
# else:
#     print("노원구")

# 127
# genderNum = input().split("-")[1][0]
# if genderNum in ["1", "3"]:
#     print("남자")
# elif genderNum in ["2", "4"]:
#     print("여자")
# else:
#     print("알수없음")


# 129
# reg_number = input().split("-")
# val = reg_number[0] + reg_number[1][:-1]
# print(val)

# index = 0
# total = 0
# new_val = list(map(int, val))
# val_num = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
# print(new_val, val_num)

# for num in new_val:
#     total += num * val_num[index]
#     index += 1

# if str(11 - (total % 11))[-1] == reg_number[1][-1]:
#     print("유효한 주민등록번호입니다")
# else:
#     print("유효하지않은 주민등록번호입니다")


# 130
import requests

btc = requests.get("https://api.bithumb.com/public/ticker/").json()["data"]
print(btc)

fluctuation = float(btc["max_price"]) - float(btc["min_price"])
if float(btc["opening_price"]) + fluctuation > float(btc["max_price"]):
    print("상승장")
else:
    print("하락장")
