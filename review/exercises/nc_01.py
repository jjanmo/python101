# variable, function

hello_world = 'hello world'
is_true = True
number = 12

print(hello_world)
print(is_true)
print(number)


def say_hello(user_name='anonymous', user_age=18):
    new_text = (
        f"Hello! {user_name} how r u\n"
        f"I'm {user_age} year's old"
    )
    print(new_text)


def say_goodbye():
    print('bye bye')


say_hello('jjanmo', 25)
say_hello()
say_goodbye()


# code challenge

def plus(a=0, b=0):
    print(a + b)


def minus(a=0, b=0):
    print(a - b)


def multiple(a=0, b=0):
    print(a * b)


def divide(a=0, b=0):
    if b == 0:
        print('zero not divided')
        return 0
    else:
        print(a / b)


def power(a=1, b=1):
    print(a ** b)


plus(1, 2)  # 3
minus(1, 2)  # -1
multiple(2, 2)  # 4
divide(4, 2)  # 2
power(3, 2)  # 9

plus()
minus()
multiple()
divide()
power()
