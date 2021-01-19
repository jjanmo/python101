# list
# => 일반적인 배열과 유사 : 여러 개의 데이터를 순서대로 저장하고 관리할 때


# 51
movie_rank = ["Dr.strange", "Split", "Lucky"]
print(movie_rank)

movie_rank.append("dark knight")
print(movie_rank)

movie_rank.insert(1, "steel of man")
print(movie_rank)

del movie_rank[3]
print(movie_rank)

lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
# lang1.append(lang2)
lang3 = lang1 + lang2
print(lang3)


num = [1, 2, 3, 4, 5, 6]
print("평균 : ", sum(num) / len(num))


price = ["20180728", 100, 130, 140, 150, 160, 170]
print(price[1:])

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("odd : ", nums[::2])
print("even : ", nums[1::2])
# print("revers : ", nums[-1::1])
print("revers : ", nums[::-1])  # 처음부터 끝까지 역방향(-1)으로


interest = ["삼성전자", "LG전자", "Naver", "SK하이닉스", "미래에셋대우"]
print(" ".join(interest))
print("/".join(interest))
print("\n".join(interest))


# join() : 자바스크립트와는 문법이 반대 ( JS : string.join('/') )

# 원형을 변형
# sort() : 기본값이 오름차순 정렬 / sort(reverse=True) 내림차순 정렬
# reverse() : 역순 정렬

# 원형은 변형하지않음 / 정렬된 새로운 객체 반환
# sorted() : 정렬된 새로운 리스트 반환
# reversed() : 뒤집힌 새로운 리스트 객체를 반환(리스트 X) -> 다시 리스트르 만들어줘야함