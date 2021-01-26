# for문
# for 변수 in list/tuple/string:
#   code here


# loop
# nums = [10, 20, 30]
# for num in nums:
#     print(num)

# values = [100, 200, 300]
# for value in values:
#     print(value + 10)

# foods = ["김밥", "라면", "튀김"]
# for food in foods:
#     print("오늘의 메뉴: " + food)

# strings = ["SK하이닉스", "삼성전자", "LG전자"]
# for string in strings:
#     print(len(string))

# animals = ["dog", "cat", "parrot"]
# for animal in animals:
#     print(f"{animal} {len(animal)}")

# for animal in animals:
#     print(animal[0])


# enmurate()
# 순서가 있는 자료형(리스트 튜플 등등)을 입력받아서 enumerate 객체를 리턴 (값과 순서를 하나의 튜플로 갖는 객체)

# numbers = [3, 4, 5]
# for index, number in enumerate(numbers):
#     # (0, 3),(1, 4),(3, 5)
#     print((index + 1) * number)


# hg = ["가", "나", "다", "라"]
# # for index, value in enumerate(hg):
# #     if index == 0:
# #         continue
# #     print(value)

# for value in hg[1:]:
#     print(value)

# print("----")

# ##역순 리스트 만들기
# for value in list(reversed(hg)):
#     print(value)

# print("----")

# for value in hg[::-1]:
#     print(value)

# print("----")

# for value in hg[0::2]:  # hg[::2]
#     print(value)


# numbers1 = [3, -20, -3, 44]

# for number in numbers1:
#     if number < 0:
#         print(number)

# numbers2 = [3, 100, 23, 44]

# for number in numbers2:
#     if number % 3 == 0:
#         print(number)

# numbers3 = [13, 21, 12, 14, 30, 18]

# for number in numbers3:
#     if (number % 3 == 0) and (number < 20):
#         print(number)

# chars = ["I", "study", "python", "language", "!"]

# for char in chars:
#     if len(char) >= 3:
#         print(char)

# animals = ["dog", "cat", "parrot"]

# for animal in animals:
#     print(animal[0].upper() + animal[1:])

# filenames = ["hello.py", "ex01.py", "intro.hwp"]

# for filename in filenames:
#     print(filename.split(".")[0])

# filenames = ["intra.h", "intra.c", "define.h", "run.py"]

# for filename in filenames:
#     extension = filename.split(".")[1]
#     # if extension == "h":
#     #     print(filename)
#     if extension == "h" or extension == "c":
#         print(filename)

# range()
# range(start, stop, step)
# start ~ stop - 1 까지의 연속된 숫자로 된 range객체를 만든다
# ex)
# range(10) [0,1,2,3,4,5,6,7,8,9] : 0부터 시작 9까지
# range(1,10,2) [1,3,,5,7,9] : 1부터 시작 9까지 2칸씩 건너뛴다

# range 객체는 반복가능한 객체를 말한다. 예) 문자열, 리스트, 딕셔너리, 세트
# 자세한 작동원리 : https://dojang.io/mod/page/view.php?id=2405
# 반복가능한 객체 안에는 __iter__ 라는 메소드가 존재 => __iter__를 실행하면 이터레이터가 실행되고
# 이터레이터에 의해서  __next__가 실행되면서 반복할 때마다 해당 요소를 순서대로 꺼낸다.
# 주의!! 반복가능한 객체와 이터레이터는 다르다!!

# for i in range(100):
#     print(i)


# for i in range(2002, 2051, 4):
#     # if i % 4 == 2: # 해줄필요없음 어차피 range에 의해서 다 걸러짐
#     #     print(i)
#     print(i)

# for i in range(1, 31):
#     if i % 3 == 0:
#         print(i)

# for i in range(3, 31, 3):
#     print(i)

# for i in range(99, -1, -1):
#     print(i)
#     print(100 - i)

# for i in range(10):
#     # print("0." + str(i))
#     print(i / 10)

# for i in range(1, 10, 2):
#     print(f"3 x {i} = {3*i}")

# sum = 0
# for i in range(1, 11):
#     sum = sum + i
# print(sum)

# odd_sum = 0
# for i in range(1, 10, 2):
#     odd_sum += i
# print(odd_sum)

# mul = 1
# for i in range(1, 11):
#     mul *= i
# print(mul)


# 171 ⭐️ 생소한 방법
# 리스트가 있음에도 for/range를 이용하는 방법
# price_list = [32100, 32150, 32000, 32500]
# for i in range(len(price_list)):
#     print(price_list[i])

# for i in range(len(price_list)):
#     print(i, price_list[i])

# for i in range(len(price_list)):
#     print(len(price_list) - 1 - i, price_list[i])


# for i in range(len(price_list) - 1):
#     print(100 + 10 * i, price_list[i])


# my_list = ["가", "나", "다", "라"]
# for i in range(len(my_list) - 1):
#     print(my_list[i : i + 2])

# my_list = ["가", "나", "다", "라", "마"]
# for i in range(len(my_list) - 2):
#     print(" ".join(my_list[i : i + 3]))

# for i in range(len(my_list) - 1, 0, -1):
#     print(my_list[i], my_list[i - 1])


# my_list = [100, 200, 400, 800]
# for i in range(len(my_list) - 1):
#     print(my_list[i + 1] - my_list[i])

# my_list = [100, 200, 400, 800, 1000, 1300]
# for i in range(len(my_list) - 2):
#     list = my_list[i : i + 3]
#     print(sum(list) / 3)

# low_prices = [100, 200, 400, 800, 1000]
# high_prices = [150, 300, 430, 880, 1000]

# volatility = []
# for i in range(len(low_prices)):
#     volatility.append(high_prices[i] - low_prices[i])
# print(volatility)


# apart = [["101호", "102호"], ["201호", "202호"], ["301호", "302호"]]
# print(apart)

# # stock = [["시가", 100, 200, 300], ["종가", 80, 210, 330]]
# stock = {"시가": [100, 200, 300], "종가": [80, 210, 330]}
# print(stock)

# stock1 = {"10/10": [80, 110, 70, 90], "10/11": [210, 230, 190, 200]}
# print(stock1)


# for i in range(len(apart)):
#     for j in apart[i]:
#         print(j)

# for row in apart:
#     for col in row:
#         print(col)

# for row in reversed(apart):
# for row in apart[::-1]:
#     for col in row:
#         print(col)

# for row in apart[::-1]:
#     for col in row[::-1]:
#         print(col)

# for row in apart:
#     for col in row:
#         print(col)
#     print("-----")

# for row in apart:
#     for col in row:
#         print(col)
# print("-----")


data = [
    [2000, 3050, 2050, 1980],
    [7500, 2050, 2050, 1980],
    [15450, 15050, 15550, 14900],
]

# 1치원 배열에 추가
# result = []
# for row in data:
#     for price in row:
#         print(price * 1.00014)
#         result.append(price * 1.00014)
#     print("-------")

# print(result)

# 2차원 배열에 추가
# result = []
# for row in data:
#     r_row = []
#     for price in row:
#         r_row.append(price * 1.00014)
#     result.append(r_row)

# print(result)


ohlc = [
    ["open", "high", "low", "close"],
    [100, 110, 70, 100],
    [200, 210, 180, 190],
    [300, 310, 300, 310],
]

# close data만 출력
# for i in range(1, 4):
#     print(ohlc[i][3])

# for row in ohlc[1:]:
#     # print(row[3])
#     if row[3] > 150:
#         print(row[3])


# for row in ohlc[1:]:
#     if row[3] >= row[0]:
#         print(row[3])

# volatility = []
# for row in ohlc[1:]:
#     diff = row[1] - row[2]
#     volatility.append(diff)
# print(volatility)


# for row in ohlc[1:]:
#     if row[3] > row[0]:
#         print(row[1] - row[2])


total = 0
for row in ohlc[1:]:
    profit = row[3] - row[0]
    total += profit
print(total)