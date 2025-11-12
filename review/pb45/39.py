# 주어진 문자열에서 6자리의 무작위코드를 중복없이 5개 생성하세요

import random

characters = "abcdefghijklnmopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

# 중복 제거에 대한 고려
# 1. seed 사용
# 2. set() 사용
# 3. 반복문 체크

# 아래처럼 난수를 생성하기 전에 seed값을 고정하면 항상 같은 순서로 난수가 생성됨
# 특정 경우(ex. 디버깅시) 같은 난수가 생성되도록 해야하는 경우가 있을수 있음
# random.seed(100)


# 나의 풀이
def solution1(n):
    coupon_codes = []

    while len(coupon_codes) < n:
        coupon_code = "".join(random.sample(list(characters), 6))
        if coupon_code not in coupon_codes:
            coupon_codes.append(coupon_code)

    return coupon_codes


result1 = solution1(6)
print(result1)


# solution1 리팩토링
def solution2(n):
    coupon_codes = set()

    while len(coupon_codes) < n:
        coupon_code = "".join(
            random.sample(characters, 6)
        )  # 문자열은 이미 시퀀스 이기때문에 list 변환이 필요없음
        # 기존에 not in 은  O(n)으로 내부적으로 n회 순회하면서 체크함
        # set을 이용한 add 는 O(1), 내부적으로 해시 기반으로 작동, 중복되는 것을 추가하려고 하면 무시(아무런 일도 발생 X)
        coupon_codes.add(coupon_code)

    return coupon_codes


result2 = solution2(6)
print(result2)
