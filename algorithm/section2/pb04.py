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
