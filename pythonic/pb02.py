# 몫과 나머지 구하기

a, b = map(int, input().strip().split(' '))  #a,b를 입력 받기
# my solution

print(int(a/b), a%b)


# pythonic solution
print(divmod(a, b))