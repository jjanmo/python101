import os
import glob


# sol1
def read_files(path):
    contents = []
    for _, _, file_names in os.walk(path):  # 순서를 보장하면서 파일을 가져오지 않는다!
        for file_name in sorted(file_names):
            with open(f"{path}/{file_name}", "r") as file:
                content = file.read()
                contents.append(content)
    return [content.strip() for content in contents]


# print(read_files("./review/pb45/27"))


# 참고 listdir() : 지정한 경로의 파일, 디렉토리를 모두 반환
# vs os.walk(path)
# → 경로의 (root, dirs, files) 을 튜플형식으로 반환
# → (현재 탐색 중인 디렉터리의 경로 (문자열),root 디렉터리 내의 하위 디렉터리 이름 목록 (리스트), root 디렉터리 내의 파일 이름 목록 (리스트))

# print(os.listdir("./review/pb45/27"))  # 이게 더 깔끔!


# sol2 glob 사용
def read_files1(path):
    contents = []
    # glob을 사용하면 경로 안의 특정 확장자명으로 파일을 가져올 수 있음
    for file in glob.glob(path + "/*.txt"):
        with open(file, "r") as f:
            content = f.read().strip()
            contents.append(content)
    return contents


print(read_files1("./review/pb45/27"))
