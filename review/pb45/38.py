# datetime 패키지와 strftime 함수를 사용해서 하단 포맷과 똑같이 출력하기

from datetime import datetime, timezone

# 타임존 출력
print(datetime.now(timezone.utc))

print("----------")

# 1. 2022-08-04 12:28:23
print("1번 포맷")
print("2022-08-04 12:28:23")
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

print("\n")

# 2. 2022-08-04 12:28:23 PM Thursday August
print("2번 포맷")
print("2022-08-04 12:28:23 PM Thursday August")
print(datetime.now().strftime("%Y-%m-%d %I:%M:%S %p %A %B"))  # %I : 12시간제 표기법

print("\n")

# 3. Thursday, August 04, 2022 12:28:57
print("3번 포맷")
print("Thursday, August 04, 2022 12:28:57")
print(datetime.now().strftime("%A, %B %d, %Y %H:%M:%S"))
print(datetime.now().strftime("%A, %B %d, %Y %T"))  # %H:%M:%S == %T

print("\n")

# 4. Thursday, Aug 08/04/22 12:28:57 PM
print("4번 포맷")
print("Thursday, Aug 08/04/22 12:28:57 PM")
print(datetime.now().strftime("%A, %b %m/%d/%y %I:%M:%S %p"))
print(
    datetime.now().strftime("%A, %b %x %r")
)  # %m/%d/%y == %x (월/일/연), %H:%M:%S %p == %r (시분초 오전/오후(12시간 표기법))
print(datetime.now().strftime("%A, %b %x %R"))  # %R 24시간 표기법

"""
참고링크 
https://docs.python.org/ko/3/library/datetime.html#strftime-strptime-behavior
"""
