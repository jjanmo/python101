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
