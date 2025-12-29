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


def getMenu():
    print("--------MENU--------")
    print("1. List Phone Book")
    print("2. Add a New Member")
    print("3. Delete a Member")
    print("4. Program Exit")


def getPhonebook():
    for item in phonebook.values():
        print(f"이름: {item['name']}")
        print(f"번호: {item['phone']}")
        print()


def addMember():
    name = input("이름: ")
    phone = input("번호: ")
    next_key = len(phonebook)
    phonebook[next_key] = {name, phone}


def deleteMember():
    name = input("이름 입력: ")
    
    

def main():
    getMenu()
    num = input("번호 선택: ")
    if num == "1":
        getPhonebook()
    elif num == "2":
        addMember()
    elif num == "3":
        


main()
