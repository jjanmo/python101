# Step1/2에서 무엇이 출력될지 생각해보기


def test(x, y):
    global a
    a = 49
    x, y = y, x
    b = 53
    b = 7
    a = 135
    # 예상1
    print("Step1 : ", a, b, x, y)  # 135, 7, 7, 23


a, b, x, y = 8, 13, 33, 44

# 함수 실행
test(23, 7)

# 예상2
print("Step2 : ", a, b, x, y)  # 135, 13, 33,44
