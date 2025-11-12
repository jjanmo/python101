# 주어진 문자열에서 6자리의 무작위코드를 중복없이 5개 생성하세요

import random

characters = "abcdefghijklnmopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

coupon_codes = []

while len(coupon_codes) < 5:
    coupon_code = "".join(random.sample(list(characters), 6))
    print(coupon_code)
    if coupon_code not in coupon_codes:
        coupon_codes.append(coupon_code)

print(coupon_codes)
