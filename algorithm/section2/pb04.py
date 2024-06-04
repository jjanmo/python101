array = [45, 73, 66, 87, 92, 67, 75, 79, 75, 80]


def get_value(scores):
    average = round(sum(scores) / len(scores))

    diff = float('inf')
    target = float("-inf")
    index = 0
    for i in range(len(scores)):
        tmp = abs(average - scores[i])
        if diff >= tmp and target < scores[i]:
            diff = tmp
            target = scores[i]
            index = i

    return [average, index + 1]


print(get_value(array))


# 파이썬에서의 round는 ROUND_HALF_EVEN 방식
# 올림과 내림이 같은 차이로 발생하는 경우 짝수쪽으로 변경되는 것을 따름
# ex. 4.5 ->  0.5 내림(4) =  0.5 올림(5) -> 같은 차이인 경우 변경된 값이 짝수인 것을 따름
# 해결책 2가지
# 1. 0.5를 더해서 int 로 정수로 변환
# 2. Decimal 이용
# 참고 : https://medium.com/@heeee/python-round-%ED%95%A8%EC%88%98%EC%99%80-round-half-even-85701f69155b


def get_value1(scores):
    average = int(sum(scores) / len(scores) + + 0.5)

    diff = float('inf')  # 평균과 각 점수와의 차이
    min_target = float("-inf")  # 평균과 가장 적게 차이나는 값
    index = 0
    for i, v in enumerate(scores):
        tmp = abs(average - v)
        if diff >= tmp and min_target < v:
            diff = tmp
            min_target = v
            index = i

    return [average, index + 1]


print(get_value1(array))

# enumerate() : iterable 객체를 받아서 인덱스와 값으로 이루어진 튜플을 반환(iterable 객체의 수만큼, 배열의 길이만큼)
