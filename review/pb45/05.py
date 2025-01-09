x = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]

y = x[4:7]  # slicing
print(y)  # ['e', 'f', 'g']

# 같은값 만들기
print(x[-9:-6])  # ['e', 'f', 'g']  # 음수 인덱스는 뒤에서 부터
print(x[4:-6])  # ['e', 'f', 'g']
print(x[-9:7])  # ['e', 'f', 'g']
print(x[-9:-6:1])  # ['e', 'f', 'g']


print(x[6:3:-1])  # ['g', 'f', 'e'] # 거꾸로!
print(reversed(x[6:3:-1]))  # reversed 의 리턴값 list_reversiterator(not list) type
print(list(reversed(x[6:3:-1])))  # ['e', 'f', 'g']

"""
[슬라이싱]
- list slicing : list[start:end:step]
"""
