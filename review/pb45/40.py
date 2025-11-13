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


main()
