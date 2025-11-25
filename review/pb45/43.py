# 43 폴더 하위에서 *.txt, *.png 파일을 분류하기
# Recursive File Extension Checker

import glob
import os


def format(txt_files, png_files):
    print(f"TXT 파일 정보 : [ {', '.join(txt_files)} ] 총 {len(txt_files)}개")
    print(f"PNG 파일 정보 : [ {', '.join(png_files)} ] 총 {len(png_files)}개")


def solution1():
    txt_files = sorted(
        list(
            map(lambda s: s.split("/")[-1], glob.glob("./43/**/*.txt", recursive=True))
        )
    )
    png_files = sorted(
        list(
            map(lambda s: s.split("/")[-1], glob.glob("./43/**/*.png", recursive=True))
        )
    )
    format(txt_files, png_files)


solution1()


result = {"txt_files": [], "png_files": []}


# 재귀를 이용하는 방법
def solution2(base_path, result):
    for file_name in os.listdir(base_path):
        full_path = os.path.join(base_path, file_name)
        if os.path.isdir(full_path):
            solution2(full_path, result)
        if os.path.isfile(full_path):
            if file_name.endswith(".txt"):
                result["txt_files"].append(file_name)
            elif file_name.endswith(".png"):
                result["png_files"].append(file_name)


solution2("./43", result)
print(result)
