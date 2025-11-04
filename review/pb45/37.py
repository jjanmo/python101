# Dictionary Search By Value

d = {
    "USA": 36,
    "Germany": 17,
    "France": 32,
    "Australia": 77,
    "South Africa": 99,
    "India": 108,
    "South Korea": 200,
}


def search_country(text):
    # sol1
    # try:
    #     lower_dict = {k.lower(): v for k, v in d.items()}  # kick!!
    #     lower_text = text.lower()
    #     return lower_dict[lower_text] # 키 값을 직접 접근시 없는 키에 접근하려고 하면 에러 발생 > except 블록으로 넘어갈수 있음
    # except:
    #     return "No results were found for your search"

    # sol2
    lower_dict = {k.lower(): v for k, v in d.items()}
    lower_text = text.lower()
    # get은 내부에서 예외처리를 해줌, 없는 키에 접근시 None 혹은 지정한 값을 리턴함
    return lower_dict.get(lower_text, "No results were found for your search")


text = input()

result = search_country(text)
print(result)
