# 1부터 15까지 원소 * 10을 한 후에 결과는 문자열 리스트로 출력하세요.
# range, map, lambda 사용
# ["10", "20", "30", "40", "50", "60", "70", "80", "90", "100", "110", "120", "130", "140", "150"]


list = list(map(lambda x: str(x * 10), range(1, 16)))
print(list)
