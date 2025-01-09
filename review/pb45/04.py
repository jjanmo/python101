# 직접 접근, index함수 사용 가능
x = ["Orange", "Cherry", "Apple", "Kiwi", "Banana", "Strawberry"]
print(x[4])  # Banana
print(x.index("Banana"))  # 4
print(x[x.index("Banana")])  # Banana
print(x.index("Cherry", 1, len(x)))  # 범위 지정(시작 1번 인덱스, 끝 6번 인덱스) → 1

#  index 함수는 값이 없을 때 예외가 발생하기때문에, 예외처리 필요!

print("Banana" in x)  # True

"""
[파이썬의 시퀀스 타입]
- 정의 : 각각의 요소들이 연속적으로 이어진 자료형
- 종류
1. 문자열(str)
2. 리스트(list)
3. 튜플(tuple)
4. 레인지(range)

"""
