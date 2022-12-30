# 문자열
msg = 'Hello World!!'
print(msg[:5])  # Hello
print(msg[6:-2])  # World
print(msg[2:])  # 2~끝까지
print(msg[:5])  # 처음부터~4까지
print(len(msg))  # 문자열 길이

for i in range(len(msg)):
    print(msg[i], end=",")
print()

for i in msg:
    print(i, end=",")
print()

text = 'I have 5 dogs!'
for i in text:
    if i.isalpha():  # 알파벳인 경우만 True
        print(i, end=' ')
print()

tmp = 'AZaz'
for i in tmp:
    print(ord(i))  # ord(문자) : 문자를 아스키넘버(유니코드)로 변환

# A → 65 | Z → 90 | a → 97 | z → 122

print(chr(65))  # chr(숫자) : 숫자를 대응되는 문자로 변환
