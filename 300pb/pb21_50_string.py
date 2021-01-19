# string

# 21
letters = "python"
print(letters[0], letters[2])

# 22
license_plate = "24가 2210"
print(license_plate[-4:])

# 23 ⭐️
string1 = "홀짝홀짝홀짝"
print(string1[0] + string1[2] + string1[4])
print(string1[::2])  # start:end:step  / 아무것도 없으면 0 or 끝 / 0부터 끝까지 스텝만큼 문자를 건너뛰면서 추출


# 24 ⭐️
print(letters[::-1])

# 25
num = "010-1111-2222"
print(num.replace("-", " "))

# 27
url = "http://sharebook.kr"
print(url.split("//")[1])

# 30
# replace()는 해당 문자를 치환한 새로운 문자열을 리턴한다. 문자열은 중간의 문자만을 바꿀수 없다.
# 문자열 -> immutable


# 32
print("hello world" * 3)
# 문자열의 곱셈 == 문자열의 반복

# 34
t1 = "python"
t2 = "java"
print((t1 + " " + t2 + " ") * 4)

# 35 ⭐️ : % operator 비추!!!
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("% operator")
print("이름 : %s 나이 : %s" % (name1, age1))
print("이름 : %s 나이 : %s" % (name2, age2))

# 36 ⭐️ : str.format
print("str.format")
print("이름 : {0} 나이 : {1}".format(name1, age1))
print("이름 : {0} 나이 : {1}".format(name2, age2))


# 37 ⭐️ : f-string
print("f-string")
print(f"이름 : {name1} 나이 : {age1}")
print(f"이름 : {name2} 나이 : {age2}")

# 38
상장주식수 = "5,969,782,550"
print(int(상장주식수.replace(",", "")))

# 39
분기 = "2020/03(E) (IFRS연결)"
print(분기.split("(")[0])

# 40
"    data      ".strip()
# 좌우 공백제거, 원본 문자열은 그대로 유지, 공백이 제거된 새로운 문자열 리턴
