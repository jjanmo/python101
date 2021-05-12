# how to import module in python

# vs in JS
# => import 이름 from 패키지


# datatime / time
import datetime

'''
datetime 모듈 안에 클래스 분류

datetime.date : 일반적으로 사용되는 그레고리안 달력의 년,월,일
datetime.time : 시간을 시,분,초,마이크로 초,시간대 정보로 나타냄
datetime.datetime : date class, time class의 조합, 년,월,일,시,분,초,마이크로 초, 시간대 정보로 나타냄
datetime.timedelta : 두 날짜/시간 사이 기간 표현
'''

print(datetime.datetime.today())  # 오늘날짜 + 지금시간
print(datetime.date.today())  # 오늘날

now = datetime.datetime.now()
print(now, type(now))  # today()와 같음



# os


# numpy

