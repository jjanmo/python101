# 아래 리스트(List)에서 apple, kiwi 를 추출해서 대문자 리스트로 출력하세요.

x = [
    "grapes",
    "mango",
    "orange",
    "peach",
    "apple",
    "lime",
    "banana",
    "cherry",
    "tomato",
    "kiwi",
    "blueberry",
    "watermelon",
]


def is_apple_or_kiwi(x):
    return x == "apple" or x == "kiwi"


def to_upper(x):
    return x.upper()


list1 = list(map(to_upper, filter(is_apple_or_kiwi, x)))
print(list1)

list2 = list(map(lambda x: x.upper(), filter(lambda x: x == "apple" or x == "kiwi", x)))
print(list2)

list22 = list(
    filter(lambda x: x == "APPLE" or x == "KIWI", map(lambda x: x.upper(), x))
)
print(list22)

list3 = []
for fruit in x:
    if fruit == "apple" or fruit == "kiwi":
        list3.append(fruit.upper())
print(list3)


list4 = []
for index in range(len(x)):
    if x[index] == "apple" or x[index] == "kiwi":
        list4.append(x[index].upper())
print(list4)


# list comprehension
list5 = [fruit.upper() for fruit in x if fruit == "apple" or fruit == "kiwi"]
print(list5)
