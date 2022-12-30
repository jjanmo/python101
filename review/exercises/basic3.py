import random

# list
a = [1, 2, 3, 4, 5]
b = list(range(5, 0, -1))
print(a, b)
c = a + b
print(c)

print(max(a))
print(min(a))
print(sum(a))
print(max(1, 5, 7))

print(a)
random.shuffle(a)
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a.clear()
print(a)

a = [23, 12, 36, 53, 19]
print(a[:3])

for i in range(len(a)):
    print(a[i], end=" ")
print()

for x in a:
    print(x, end=" ")
print()

print(enumerate(a))
for x in enumerate(a):  # 튜플 형식 (0, 23),....(4, 19)
    print(x)
    print(x[0], x[1])
print()

for index, value in enumerate(a):
    print(index, value)

if all(60 > x for x in a):  # all : 모두 참인 경우 전체적으로 True
    print('YES')
else:
    print('NO')

if any(50 < x for x in a):  # any : 한번이라도 참이면 전체적으로 True
    print('YES')
else:
    print('NO')

# 2차원 리스트

arr1 = [0] * 5
print(arr1)

arr2 = [[0] * 5 for _ in range(5)]
print(arr2)

for row, value1 in enumerate(arr2):
    print(f'row:{row} →', end=" ")
    for col, value2 in enumerate(value1):
        print(f'index:{col}, value:{value2}', end=' ')
    print()
