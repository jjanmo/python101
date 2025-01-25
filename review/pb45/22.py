# 22-2.txt 파일을 공백 구분 후 단어 개수를 출력하는 함수
# 콤마의 경우 두 단어로 취급 ex. Hi! Kim,Eun 의 경우 -> 3개
# 72

import re


def read_file(path):
    with open(path, "r") as file:
        content = file.read()
        content = content.replace(",", " ").split(" ")
        return len(content)


result = read_file("./review/pb45/22.txt")  # 컴파일이 돌아가는 경로 기준으로 경로를 작성해야함
print(result)


def read_file_with_regex(path):
    with open(path, "r") as file:
        content = file.read()
        content = re.split(" |,", content)  # 정규표현식 사용
        return len(content)


result = read_file_with_regex("./review/pb45/22.txt")
print(result)
