# 파일 입출력과 예외처리
# 291 ~ 300

# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# file : 파일경로
# mode : r(read) required / w(write) / t(text) default / +(update) / a 파일 마지막에 새로운 내용을 추가할 때
# 파일 객체는 반드시 열고 작업이 완료되면 파일을 닫아야 한다. ( close() )

# f = open('./매수종목.txt', 'w')
f = open('./bidding-coins.txt', mode='wt', encoding='utf-8') # encoding 써주는 것이 좋다
data = 'BTC 비트코인\nETH 이더리움\nDOGE 도지코인\nBTT 비트토렌트\nXRP 리플'
f.write(data)
f.close()

import csv

f =open('./bidding-coins.csv', mode='wt', newline="") #cp949
wr = csv.writer(f)
# wr.writerows([[1,'BTC', '비트코인'],[2,'ETH','이더리움'],[3,'DOGE','도지코인'],[4,'BTT','비트토렌트'],[5,'XRP','리플']])
wr.writerow([1,'BTC', '비트코인'])
wr.writerow([2,'ETH','이더리움'])
wr.writerow([3,'DOGE','도지코인'])
f.close()


f = open('./list.txt', mode='r')
# while True:
#   line = f.readline()
#   print(line)
#   if not line:
#     break

lines = f.readlines() # lines => list
for line in lines:
  print(line.strip()) # strip -> same as trim() in JS
f.close()


f = open('./coins.txt', mode='r', encoding='utf-8')
lines = f.readlines()
coins = {}
for line in lines:
  symbol, name = line.split()
  coins[symbol] = name

print(coins)
f.close()


per = ["10.31", "", "8.00"]
list = []
for i in per:
    try:
      # 이렇게 사용해도 number의 스코프는 전역변수 / 함수나 클래스 내에서 사용되는 것만 지역변수
      # 자바스크립트와는 다르게 파이썬에서는 스코프 블록 개념이 함수나 클래스를 나타냄, 인덴트는 상관없음(개인적인 착각)
      number = float(i) 
    except:
      number = 0
    finally:
      list.append(number)
print(list)



number = 17
try:
  number / 0
except ZeroDivisionError as e:
  print(e)


data = [1, 2, 3]
for i in range(5):
  try:
      print(data[i])
  except IndexError as e:
      print(e)



per = ["10.31", "", "8.00"]
for i in per:
    try:
      number = float(i)
    except:
      number = 0
      print('오류입니다.')
    else:
      print('오류가 아닙니다.')
    finally:
      print(number)
