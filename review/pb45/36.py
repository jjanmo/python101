# Progressive Time Delays to Code
# interval을 0.5초 ~ 3초까지 0.5초 간격으로 딜레이를 증가하면서 출력하는

import time


def solution():
    interval = 0.5
    while interval <= 3:
        time.sleep(interval)
        print(f"Delayed for {interval} seconds")
        interval = interval + 0.5


solution()
