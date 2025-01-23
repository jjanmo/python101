# 아래와 같은 Dict 구조에서 모든 value 값의 합(Sum)을 구하세요
# 가능한 모든 방법
# 출력결과 : 2327


d = {"a": 17, "b": 114, "c": 247, "d": 362, "e": 220, "f": 728, "g": -283, "h": 922}


# sol1
sum1 = 0
for value in d.values():
    sum1 += value
print(sum1)

# sol2
from functools import reduce

sum2 = reduce(lambda acc, cur: acc + cur, d.values(), 0)
print(sum2)

# sol3
print(sum(d.values()))
