# dictionery : key / value 형태로 데이터 저장


a, b, *c = (0, 1, 2, 3, 4, 5)
print(a, b, c)
# 기본적으로 튜플은 언패킹시에 좌변과 우변의 개수가 같아야 한다. (언패킹은 튜플뿐만 아니라 리스트에서도 가능하다)
# 하지만  *를 사용하면 개수가 달라도 언패킹을 할 수 있다.
# c는 [2,3,4,5] 를 나타낸다

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# tScores = tuple(scores) # 데이터 언패킹은 리스트에서도 가능
# valid_score = tScores[:8]
# print(valid_score)

*valid_score1, _, _ = scores
print("1", valid_score1)

_, _, *valid_score2 = scores
print("2", valid_score2)


tmp = {}
print(type(tmp))

icecream = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
print(icecream)

icecream.update({"죠스바": 1200, "월드콘": 1500})
print(icecream)

icecream["메로나"] = 1300
print(icecream)

del icecream["메로나"]
print(icecream)

invenetory = {
    "메로나": {"가격": 300, "재고": 20},
    "비비빅": {"가격": 400, "재고": 3},
    "죠스바": {"가격": 250, "재고": 100},
}

print(invenetory)

print(invenetory["메로나"]["가격"], "원")
print(invenetory["메로나"]["재고"], "개")

invenetory["월드콘"] = {"가격": 500, "재고": 7}

print(invenetory)

# 딕셔너리 병합 방법 2가지
# 1) icecream.update(invenetory)
# 2)
newIcecream = dict(icecream, **invenetory)
print(newIcecream)

print(type(newIcecream.keys()))  # type dict_key ??
print(list(newIcecream.keys()))


icecream2 = {"탱크보이": 1200, "폴라포": 1200, "빵빠레": 1800, "월드콘": 1500, "메로나": 1000}
print(sum(icecream2.values()))


keys = ("apple", "pear", "peach")
vals = (300, 250, 400)

# zip : 반복 가능한 객체 여러 개를 넣으면 요소 순서대로 "튜플"로 묶어서 "zip 객체"를 반환 => 리스트/딕셔너리로 변환
print(list(zip([1, 2, 3], [10, 20, 30])))  # [(1, 10), (2, 20), (3, 30)]
print(dict(zip((1, 2, 3), (10, 20, 30))))  # {1: 10, 2: 20, 3: 30}


# 딕셔너리 만드는 방법
# 1)
dict1 = {"age": 14, "name": "jjanmo"}
print("dict1", dict1)

# 2)
dict2 = dict({"age": 14, "name": "jjanmo"})
print("dict2", dict2)

# 3
dict3 = dict(age=14, name="jjanmo")
print("dict3", dict3)

# 4
dict4 = dict(zip(["age", "name"], [14, "jjanmo"]))
print("dict4", dict4)

# 5
dict5 = dict([("age", 14), ("name", "jjanmo")])
print("dict5", dict5)


keys = ("apple", "pear", "peach")
vals = (300, 250, 400)

print(dict(zip(keys, vals)))

date = ["09/05", "09/06", "09/07", "09/08", "09/09"]
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))
print(close_table)