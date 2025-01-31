# 여러가지 String format

x = 10
y = 20
serialno = 308276567
n = "Kim"


# 출력1 : % Operator(old style)
ex1 = "n = %s, s = %d, sum=%d" % (n, serialno, (x + y))
print(ex1)  # %s, %x, %d 에 순서대로  % 뒤의 변수가 들어감
"""
각각 문자의 의미
%s : 문자열(string)을 나타내는 포맷
%d : 정수(integer)를 나타내는 포맷 
%f : 부동소수점(실수)(float)을 나타내는 포맷
%x,%X : 16진수(hexadecimal)을 나타내는 포맷으로 x는 소문자, X는 대문자로 출력

단, 위는 타입에 대한 강제성은 없기때문에 사실상 %s로 다 적어도 문제없이 작동한다.
"""


# 출력2 : format
ex2 = "n = {n}, s = {serialno}, sum={sum}".format(n=n, serialno=serialno, sum=x + y)
print(ex2)  # format 인자가 순서대로 들어감


# 출력3 : f string
ex3 = f"n = {n}, s = {serialno}, sum={x + y}"
print(ex3)  # js의 template literal 과 같은 방식


# 출력4 :  template string

from string import Template

ex4 = "n = $n, s = $serialno, sum=$sum"
template = Template(ex4)  # ex4 스타일의 템플릿을 생성
result = template.substitute(
    n=n, serialno=serialno, sum=x + y
)  # 위에서 선언한 template에 맞게 변수를 인자로 넣어준다
print(result)


# f string을 가장 많이 추천함! 다만 버전이 맞아야하는 조건이 있음(python 3.6+)
# → 가독성, 성능이 가장 좋음


# f string 포맷팅 규칙들

# 1) 너비 지정

name = "jjanmo"

print(f"'{name:10}'")  # 10칸 너비
print(f"'{name:20}'")  # 20칸 너비
print(f"{name:<10}")  # 왼쪽정렬
print(f"{name:^10}")  # 가운데정렬
print(f"{name:>10}")  # 오른쪽정렬

pi = 3.14
print(f"{pi:.2f}")  # 소수점 2자리
print(f"{pi:.3f}")  # 소수점 3자리
print(f"{name:.3}")  # 문자열에서 3글자만 출력

num = 255
print(f"{num:b}")  # 2진수 binary
print(f"{num:o}")  # 8진수 octal
print(f"{num:x}")  # 16진수 소문자
print(f"{num:X}")  # 16진수 대문자
