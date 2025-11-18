# 텍스트 파일을 불러온 후 알파벳 C로 시작하는 나라의 지표의 합을 출력


def solution1():
    sum = 0
    with open("41.txt", "r") as f:
        content = f.read()
        splitted = content.split("\n")

        for item in splitted:
            if item.startswith("C"):
                sum = sum + int(item.split(",")[1])

    return sum


# result = solution1()
# print(result) # 1546447728


def convert(line):
    if line.lower().startswith("c"):
        _, value = line.split(",")
        return int(
            value.rstrip()
        )  # 문자열(string)의 오른쪽 끝에서 특정 문자(또는 공백)를 제거하는 메소드 (cf.lstrip(왼쪽), strip(양쪽))
    else:
        return 0


def solution2(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

        return list(map(convert, lines))


result = solution2("./41.txt")
print(sum(result))  # 1546447728
