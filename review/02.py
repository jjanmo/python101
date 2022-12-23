# control flow
import random
import math

my_value = 500

def who_winner(value):
  if value <= 50:
    print('if')
  elif value < 100:
    print('elif1')
  elif value < 200:
    print('elif2')
  elif value < 300:
    print('elif3')
  else:
    print('else')
    
who_winner(my_value)


# EX1)
# def calc_drinkable():
#   age = int(input('당신의 나이를 입력하세요'))

#   if age < 20:
#     print('20살 미만은 음주할 수 없습니다. 😡')
#   elif age >= 20 and age < 40:
#     print('술먹기 좋은 나이지 ~ 🍺')
#   else:
#     print('이제 술을 멀리하시길 추천드립니다. 🙏')
  

# calc_drinkable()



# EX2)
def play_casino():
  choice = int(input('1 ~ 10 사이의 숫자를 선택하세요'))
  computer = math.floor(random.random()*10 + 1)
  
  if choice == computer:
    print('축하합니다! 맞았습니다 😎')
  else:
    print('땡!! 꽝입니다. 🙃')
    print(f'당첨번호는 {computer} 입니다')


play_casino()