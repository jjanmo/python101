import os


def write_txts(path, names, contents):
    if not os.path.exists(path):  # 폴더 유무 확인
        os.makedirs(path)

    for name, content in zip(names, contents):
        with open(f"{path}/{name}.txt", "w") as file:
            file.write(content)


file_names = ["A", "B", "C", "D", "F", "G"]
file_contents = ["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"]


write_txts("./review/pb45/26", file_names, file_contents)


# 참고 file.writelines() : write a list of strings to a file at once.
# → ["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"] 요런 리스트를 내부적으로 순회하면서 하나의 파일에 추가하게됨
