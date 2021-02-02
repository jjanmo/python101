test1 = [[1], [2]]
test2 =[[1, 2], [3, 4], [5]]

# my solution
def my_solution(mylist):
    answer = []
    for i in mylist:
        answer.append(len(i))
    return answer

print(my_solution(test1))
print(my_solution(test2))

# pythonic solution
def pythonic_solution(mylist):
    return list(map(len, mylist))

print(pythonic_solution(test1))
print(pythonic_solution(test2))