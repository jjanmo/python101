# 1부터 20까지 홀수 * 10, 짝수는 그대로 리스트로 출력하세요.
# [10, 2, 30, 4, 50, 6, 70, 8, 90, 10, 110, 12, 130, 14, 150, 16, 170, 18, 190, 20]


def operate(num):
    if num % 2 == 1:
        return num * 10
    else:
        return num


list = list(map(operate, list(range(1, 21))))
print(list)


# list comprehension : 짧은 문법으로 간단하게 조건에 맞는 리스트 생성(방법 3가지)
# [x for x in list]
# [x for x in list if condition]
# [condition_true_value if condition else condition_false_value for x in list]

list1 = [x if x % 2 == 0 else x * 10 for x in range(1, 21)]
print(list1)

# 참고 리스트 컴프리헨션을 사용한 "이중리스트" 만들기
print([[i for i in range(0, 5)] for i in range(0, 5)])
