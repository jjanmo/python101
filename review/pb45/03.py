x = "Seoul"
y = 25
# z = x + y  ## 파이썬에서는 문자열과 숫자를 더할 수 없다 (unlike javascript) : type error
z = x + str(y)

print(f"x + y : {z}")


"""
[형변환 방법]
1. 문자열 형변환 : str()
2. 숫자 형변환 : int(), float()
3. 리스트 형변환 : list()
4. 튜플 형변환 : tuple()
5. 집합 형변환 : set()
6. 딕셔너리 형변환 : dict()
7. 불리언 형변환 : bool()
"""


"""
[파이썬 주요 에러]
1. type erro : type casting (위 내용)
2. calling a non-callable
3. list index
"""

# 2. calling a non-callable
str = "hello"
# print(str()) # TypeError: 'str' object is not callable


# 3. list index
arr = [1, 2, 3, 4, 5]
print(arr[3])  # 4
# print(arr[5])  # IndexError: list index out of range
