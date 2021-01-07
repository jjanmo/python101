# 파이썬은 7개의 연산자를 지원한다.

# 산술연산자
# 1) 사칙연산자 : + -  * /(진짜 나누기)
# 2) 제곱 : **
# 3) 나머지 : %
# 4) // : 몫

print(3 ** 4)  # 3의 4승
print(5 % 2)  # 1
print(5 / 2)  # 2.5
print(5 // 2)  # 1


# 비교연산자(관계연산자)
# == != < > <=  >=
# 비교에 의한 True / False 값 반환

# 할당연산자
# 변수에 값을 할당하기 위해서 사용
# = += -= *= /= %= //=
# 산술연산자를 모두 = 을 붙여서 할당연산자처럼 만들수 있다.

a = 10
a *= 4
print(a)  # 40

b = 12
b /= 5
print(b)

c = 14
c %= 4
print(c)

d = 17
d //= 2
print(d)

# 논리연산자
# and, or, not

# Bitwise 연산자
# &(AND), |(OR), ^(XOR), ~(Complement), <<, >>(Shift)
# 실제 활용을 통해서 알아보자


# 멤버쉽 연산자 : 포함 여부 판별
# in, not in
a = ["javascript", "java", "python"]
b = "rust" in a  # False
c = "python" in a  # True
d = "java" not in a  # True
print(b, c, d)


# Identity 연산자 : 양쪽의 Operand의 동일 여부 판별
# is, is not
name = "jjanmo"
nickname = name
isSame = name is nickname
print(isSame)  # True

## 참고
# Identity 연산자 : is / is not => 객체 비교
# 비교 연산자 : == / != => 값 비교
