# 아래와 리스트에서 중복되는 원소를 제거 후 출력하세요.
# 다양한 방법
# 결과 [1, 2, 3, 4, 5, 'a', 'b']

x = ["a", 1, "b", 2, "a", 3, "b", 4, 5, "b"]

# sol1
list1 = []
for i in x:
    if i not in list1:
        list1.append(i)

print(sorted(list1, key=str))


# sol2
list2 = list(set(x))
print(sorted(list2, key=str))
