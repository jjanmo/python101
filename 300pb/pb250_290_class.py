# class

"""
Class
=> 큰 틀
Object
=> 클래스로부터 생성된 것
Instance
=> 객체와 같은 의미지만, 클래스와 객체와의 관계에 대해서 의미한다면 인스턴스라고 사용함
"""


class Human:  # 클래스
    def __init__(self, name, age, gender):  # 생성자 / 생성자 함수는 인스턴스가 생성될 때 실행된다.
        self.name = name  # 생성자 함수에서 인자를 받음으로서 객체 생성에서의 초기값으로 설정할 수 있다.
        self.age = age
        self.gender = gender
        print("응애 응애")

    def who(self):
        print("이름은", self.name)
        print("나이는", self.age)
        print("성별은", self.gender)

    def setInfo(self, name, age, gender):  # setter 메소드와 같다.
        self.name = name
        self.age = age
        self.gender = gender

    def __del__(self):  # 소멸자 : 객체가 소멸되었음을 알리는 메소드
        print("나의 죽음을 알리지 말라")


jjanmo = Human("짠모", 25, "남자")  # jjanmo는 객체이자, 클래스 Human의 인스턴스이다
jjanmo.who()
print(jjanmo.name)  # 생성된 객체를 통해서 name변수에 접근할 수 있다

jjanmo.setInfo("혜리", 30, "여자")
jjanmo.who()

del jjanmo