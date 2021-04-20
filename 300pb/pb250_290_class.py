# class

# 271 ~ 280
"""
Class
=> 큰 틀
Object
=> 클래스로부터 생성된 것
Instance
=> 객체와 같은 의미지만, 클래스와 객체와의 관계에 대해서 의미한다면 인스턴스라고 사용함
"""


class Human:  # 클래스
    def __init__(self, name, age, gender):  # 생성자는 객체(인스턴스)가 생성될 때 실행되는 메소드
        self.name = name  # 생성자 함수에서 인자를 받음으로서 객체 생성에서의 초기값으로 설정할 수 있다.
        self.age = age
        self.gender = gender
        print("응애 응애")

    # self
    # 인스턴스 자기자신, 생성된 객체 자신

    def who(self):
        print("이름은", self.name)
        print("나이는", self.age)
        print("성별은", self.gender)

    def set_info(self, name, age, gender):  # setter 메소드와 같다.
        self.name = name
        self.age = age
        self.gender = gender

    def __del__(self):  # 소멸자 : 객체가 소멸될 때 호출되는 메소드
        print("나의 죽음을 알리지 말라")


jjanmo = Human("짠모", 25, "남자")  # jjanmo는 객체이자, 클래스 Human의 인스턴스이다
jjanmo.who()
print(jjanmo.name)  # 생성된 객체를 통해서 name변수에 접근할 수 있다

jjanmo.set_info("혜리", 30, "여자")
jjanmo.who()

del jjanmo


# 271 ~ 280

class Stock:
    def __init__(self, name, code, per, pbr, dividend_yield):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend_yield = dividend_yield  # 배당 수익률

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_dividend_yield(self, dividend_yield):
        self.dividend_yield = dividend_yield


# samsung = Stock("삼성전자", "005930")
# print(type(samsung))
# print(samsung.name)
# print(samsung.code)


# a = Stock(None, None)
# a.set_name("삼성전자")
# print(a.name)
#
# b = Stock(None, None)
# b.set_code(005930)
# print(b.code)
#
# c = Stock("셀트리온", 068270)
# print(c.get_name())
# print(c.get_code())

d = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
print(d.name)
print(d.code)
print(d.per)
print(d.pbr)
print(d.dividend_yield)
d.set_per(12.75)
print(d.per)

ss = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
hd = Stock("현대차", "005380", 8.70, 0.35, 4.27)
lg = Stock("LG전자", "066570", 317.34, 0.69, 1.37)
print("---------")
stocks = [ss, hd, lg]
for obj in stocks:
    print("PER", obj.per)


# 271 ~ 280
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"


# 281 ~ 290
class Car:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price
    
    def log_info(self):
        print('바퀴수 : ', self.wheel)
        print('가격 : ' , self.price)

my_car = Car(2, 1000)
print(my_car)
print(my_car.wheel)
print(my_car.price)


class Bike(Car):
    def __init__(self, wheel, price, drivetrain):
        super().__init__(wheel, price) # 부모의 속성을 가져와서 사용
        self.drivetrain = drivetrain

    def log_info(self):
        super().log_info()
        print(self.drivetrain)
# my_bike = Bike(2, 100)
# print(my_bike.wheel)
# print(my_bike.price)

my_bike = Bike(2, 100, '시마노')
print(my_bike.price)
print(my_bike.drivetrain)
print('my bike')
my_bike.log_info()

class SuperCar(Car):
    def __init__(self, wheel, price):
        super().__init__(wheel, price)

    # def log_info(self):
    #     print('바퀴수 : ', self.wheel)
    #     print('가격 : ' , self.price)

car = SuperCar(4, 1000)
print('super car')
car.log_info()


# method overriding
class 부모:
  def 호출(self):
    print("부모 호출")

class 자식(부모):
  def 호출(self):
    print("자식 호출")

나 = 자식()
나.호출()    # 자식 호출

print('---------')


# # constructor1
# class 부모:
#   def __init__(self):
#     print("부모 생성")

# class 자식(부모):
#   def __init__(self): # 부모의 __inti__ overriding
#     print("자식 생성")

# 나 = 자식()  # 자식 생성

print('---------')

# constructor2
class 부모:
  def __init__(self):
    print("부모 생성")

class 자식(부모):
  def __init__(self):
    print("자식 생성")
    super().__init__() # 부모 클래스에 있는 것을 (오버라이딩 시키지 않고) 호출하고 싶다면 명시적으로 적어줘야한다.

나 = 자식()  # 자식 생성 부모 생성
