while True:
    key = input("메뉴\n1. 쓰기\n2. 읽기\n3. 종료\n>> 번호를 고르세요 :  ")

    if key == "1":
        with open("./44.txt", "a+") as f:
            f.seek(0)
            content = f.read()
            if content != "":
                print("[이전에 입력한 내용]")
                print(">>>>>>")
                print(content)
                print(">>>>>>")
            print("🎬 글쓰기 시작")
            text = input()
            f.write("\n" + text)
            print("\n✅ 글쓰기 완료")
    elif key == "2":
        with open("./44.txt", "r") as f:
            content = f.read()
            print("[입력한 내용]")
            print(">>>>>>")
            print(content)
            print(">>>>>>")
            print("\n✅ 파일 읽기 완료")
    elif key == "3":
        print(key)
        break
