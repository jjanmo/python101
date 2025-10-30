colors = ["red", "green", "black", "blue", "orange", "purple"]

dict1 = {}
dict2 = {}
for i, color in enumerate(colors):
    dict1[i] = color
    dict2[i + 100] = color

print(f"dict1 : {dict1} \n dict2 : {dict2}")

print("다른 방법")
print(dict(enumerate(colors)))
print(dict(enumerate(colors, 100)))


# for문에서 index를 같이 활용하고 싶을때 enumerate() 를 사용할 수 있음
# → enumerate() 는 열거형 객체를 반환하고 카운터 변수도 추가해줌
# → enumerate(iterable, index의 시작값(기본값 0))
