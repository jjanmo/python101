# tuple = (1, 2, 3, 4) or  1, 2, 3, 4
# 불변한 순서가 있는 객체의 집합
# 리스트와 비슷하지만, 한 번 생성되면 값을 변경할 수 없다.


my_tuple = ()
print(my_tuple, type(my_tuple))

movie_rank = "Dr.Strange", "Split", "Lucky"
# ("Dr.Strange", "Split", "Lucky")
print(type(movie_rank))

num1 = 1
num2 = (1,)
num3 = 1
num4 = (1,)
print(
    "num1 : ",
    type(num1),  # int
    "num2 : ",
    type(num2),  # tuple
    "num3 : ",
    type(num3),  # int
    "num4 : ",
    type(num4),  # tuple
)


interest = ("삼성전자", "LG전자", "SK Hynix")
new_interest = list(interest)
print(type(new_interest))

new_tuple = tuple(new_interest)
print(type(new_tuple))


# tuple unpacking
tmp = ("cake", "apple", "banana")
a, b, c = tmp
print(a, b, c)


# nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
# print(nums[1::2])

# range() : 연속된 정수를 만들어주는 함수
# 1 부터 99까지의 정수 중 짝수만 저장된 튜플을 생성하라.
print(tuple(range(2, 100, 2)))

# print(list(range(2, 100, 2)))
