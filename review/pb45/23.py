# 파일명 & 경로 = "../source/23-1.txt"
# 파일 출력 결과 : "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"

import string


def write_file(path):
    with open(path, "w") as file:
        alphabet = list(string.ascii_uppercase)
        text = " ".join(alphabet)
        file.write(text)


def read_file(path):
    with open(path, "r") as file:
        content = file.read()
        print(content)


write_file("./review/pb45/23.txt")
read_file("./review/pb45/23.txt")


print("###########")
# 알파벳을 쉽게 만드는 방법

# sol1
# string package를 이용
upper = list(string.ascii_uppercase)  # string.ascii_uppercase : A~Z 까지 문자열로 선언되어있음
lower = list(string.ascii_lowercase)
print(upper, end="\n")
print(lower, end="\n")

# sol2
# ord() : 알파벳을 아스키코드인 숫자로 변환
# chr() : 아스키코드 숫자를 알파벳으로 변환

list1 = []
for i in range(ord("A"), ord("Z") + 1):
    list1.append(chr(i))
print(list1, end="\n")

list2 = [chr(i) for i in range(ord("A"), ord("Z") + 1)]  # 한줄 코드로도 쓸 수 있음
print(list2, end="\n")
