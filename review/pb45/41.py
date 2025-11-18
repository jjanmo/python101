# 텍스트 파일을 불러온 후 알파벳 C로 시작하는 나라의 지표의 합을 출력


def solution():
    sum = 0
    with open("41.txt", "r") as f:
        content = f.read()
        splitted = content.split("\n")

        for item in splitted:
            if item.startswith("C"):
                sum = sum + int(item.split(",")[1])

    return sum


result = solution()
print(result)
