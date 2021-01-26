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

filenames = ["intra.h", "intra.c", "define.h", "run.py"]

for filename in filenames:
    extension = filename.split(".")[1]
    # if extension == "h":
    #     print(filename)
    if extension == "h" or extension == "c":
        print(filename)
