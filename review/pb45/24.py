# 출력 결과 : "{'one': 156.0, 'two': 148.0, 'three': 54.0, 'four': 315.0}"

a = ["one", "two", "three", "four"]
b = [30, 20, 15, 75]
c = [5.2, 7.4, 3.6, 4.2]

# sol1
result1 = {}
for i, v in enumerate(a):
    result1[v] = b[i] * c[i]
print(result1)

# sol2
result2 = {}
for av, bv, cv in zip(a, b, c):
    result2[av] = bv * cv
print(result2)

# sol3
mul = [bvv * cvv for bvv, cvv in zip(b, c)]
print(dict(zip(a, mul)))

# sol4
print({x: y * z for x, y, z in zip(a, b, c)})  # 👍🏻


# zip(iterate ... , strict=True) → strict는 길이가 다른 리스트를 묶을 때 에러가 발생

list1 = [1, 2, 3]
list2 = [4, 5]

# ValueError: zip() argument 2 is shorter than argument 1
# zipped = zip(list1, list2, strict=True)
# print(list(zipped))

# False인 경우는 list의 길이가 짧은 것을 기준으로 묶고 나머지는 무시된다.
zipped = zip(list1, list2, strict=False)
print(list(zipped))  # [(1, 4), (2, 5)]
