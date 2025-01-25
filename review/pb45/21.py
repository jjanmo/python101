# in_str = "Suppose we have few words that are separated by spaces."
# 출력 결과 : 10


def count_str():
    sentence = input()
    splited = sentence.strip().split(" ")  # split() 기본 seperator 는 공백
    print(splited)
    return len(splited)


print(count_str())


# split(seperator, maxsplit)

s = "banana&cherry&kiwi&orange"
# maxsplit 만큼만 자름
a = s.split("&", 1)
print(a)  # ['banana', 'cherry&kiwi&orange']
b = s.split("&", 2)
print(b)  # ['banana', 'cherry', 'kiwi&orange']
c = s.split("&", 3)
print(c)  # ['banana', 'cherry', 'kiwi', 'orange']
