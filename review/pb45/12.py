# 아래와 같이 Dictionary 에 {'c': 'banana', 'd': 'kiwi'}를 추가하세요.
# 가능한 방법 모두
# 결과  {'a': 'apple', 'b': 'grape', 'c': 'banana', 'd': 'kiwi'}

d = {'a': 'apple', 'b': 'grape'}

# sol1
d1 = {'a': 'apple', 'b': 'grape'}
d1.update({'c': 'banana', 'd': 'kiwi'})
print(d1)


# sol2
target = {'a': 'apple', 'b': 'grape'}
source = {'c': 'banana', 'd': 'kiwi'}
for key in source:
  target[key] = source[key]
print(target)


