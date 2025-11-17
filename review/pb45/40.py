# 비밀번호 유효성 검사

"""
조건1 비밀번호는 반드시 8글자
조건2 반드시 1개 이상의 대문자 포함
조건3 반드시 1개 이상의 숫자 포함
"""

import re


def validate(password):
    if len(password) < 8:
        return False, "비밀번호는 반드시 8자 이상이여야합니다."

    if not re.search(r"[A-Z]", password):
        return False, "비밀번호는 반드시 1개 이상의 대문자를 포함해야합니다."

    if not re.search(r"[0-9]", password):
        return False, "비밀번호는 반드시 1개 이상의 숫자를 포함해야합니다."

    return True, "비밀번호 조건에 맞습니다."


def main():
    while True:
        password = input("비밀번호를 입력하세요: ")
        is_valid, message = validate(password)
        if is_valid:
            print(f"입력된 비밀번호 : {password} > {message}")
            return
        else:
            print(message)


# main()


def solution():
    error_messages = []
    while True:
        password = input("비밀번호를 입력하세요: ")

        # c.isdigit() for c in password : 제너레이터 iterable > 제너레이터 표현식으로 만들어진 반복 가능한 객체로서 필요한 순간에 하나씩 계산하면서 반복할 수 있는 객체
        # vs 리스트 컴프리헨션( [c.isdigit() for c in password] )  : 모든 값을 리스트에 저장하기 때문에 메모리를 제너레이터 iterable 보다 더 많이 사용함
        # any(iterable) : 인자로 iterable이 들어올수 있기 때문에 아래처럼 표현 가능
        if not any(c.isdigit() for c in password):
            error_messages.append("비밀번호는 반드시 1개 이상의 숫자를 포함해야합니다.")

        if not any(c.isupper() for c in password):
            error_messages.append(
                "비밀번호는 반드시 1개 이상의 대문자를 포함해야합니다."
            )

        if len(password) < 8:
            error_messages.append("비밀번호는 반드시 8자 이상이여야합니다.")

        if len(error_messages) == 0:
            print("비밀번호 조건에 맞습니다.")
            return
        else:
            for message in error_messages:
                print(f"· {message}")
            error_messages = []


solution()
