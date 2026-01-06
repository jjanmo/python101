# Phone Book Project
"""
구현내용
조건1 : 전화번호부 확인
조건2 : 전화번호부 멤버 추가
조건3 : 전화번호부 멤버 삭제
조건4 : 프로그램 종료
조건5 : 전화번호 전체 데이터는 아래와 같이 json 형식으로 가정
조건6 : (가능한경우) 파일 쓰기, 읽기 기능 추가
"""

phonebook = {
    0: {"name": "Kim", "phone": "45648733"},
    1: {"name": "Lee", "phone": "89376333"},
    2: {"name": "Park", "phone": "36457818"},
    3: {"name": "Chung", "phone": "76891234"},
    4: {"name": "Choi", "phone": "67451237"},
}


def check_name(name):
    for item in phonebook.values():
        if item["name"] == name:
            return True
    return False


def check_phone(phone):
    for item in phonebook.values():
        if item["phone"] == phone:
            return True
    return False


def find_items_by_name(name):
    targets = []
    for key, item in phonebook.items():
        if item["name"] == name:
            targets.append({"key": key, "name": item["name"], "phone": item["phone"]})
    return targets


def find_item_by_phone(phone, data):
    for item in data:
        if item["phone"] == phone:
            return item
    return None


def print_menu():
    print("--------MENU--------")
    print("1. List Phone Book")
    print("2. Add a New Member")
    print("3. Delete a Member")
    print("4. Program Exit")


def print_phonebook():
    for item in phonebook.values():
        print(f"이름: {item['name']}")
        print(f"번호: {item['phone']}")
        print()


def add_member():
    name = input("이름: ")
    phone = input("번호: ")

    is_existed = check_phone(phone)
    if is_existed == True:
        print("이미 존재하는 번호입니다.")
        return

    next_key = len(phonebook)
    phonebook[next_key] = {"name": name, "phone": phone}
    print("멤버가 등록되었습니다.")


def delete_member():
    name = input("이름 입력: ")
    items = find_items_by_name(name)
    if len(items) == 0:
        print("입력하신 이름의 멤버는 존재하지 않습니다.")
        return

    phone = input("번호 ")
    finded_item = find_item_by_phone(phone, items)
    if finded_item == None:
        print("입력하신 번호를 가진 멤버는 존재하지 않습니다.")
        return

    del phonebook[finded_item["key"]]
    print("삭제가 완료되었습니다.")


def main():
    while True:
        print_menu()
        num = input("번호 선택: ")
        if num == "1":
            print_phonebook()
        elif num == "2":
            add_member()
        elif num == "3":
            delete_member()
        elif num == "4":
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 번호를 선택하세요.")


main()
