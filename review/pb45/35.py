# Time Delays to Code
# 1 ~ 10 까지 1초 간격으로 호출

import threading
import time


def solution1():
    count = 1
    while True:
        print(count)
        count = count + 1
        if count > 10:
            return
        time.sleep(1)


solution1()
