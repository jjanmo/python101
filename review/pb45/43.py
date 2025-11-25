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


def solution3():
    for results in os.walk("./43"):
        """
        os.walk("./43") 의 결과값 : 튜플
        ('./43', ['sub1', 'sub2'], ['file2.txt', 'file8.py', 'file1.txt', 'file5.txt', 'file7.txt', 'file20.txt', 'file19.png', 'file12.py', 'file13.py', 'file3.py', 'file17.py', 'file6.png', 'file10.png', 'file4.py', 'file18.dll', 'file11.png', 'file9.txt', 'file16.bin', 'file14.txt', 'file15.txt'])
        ('./43/sub1', [], ['file1.txt', 'file6.bin', 'file2.py', 'file3.png', 'file7.png', 'file4.py', 'file5.py'])
        ('./43/sub2', [], ['file7.txt', 'file6.txt', 'file2.py', 'file3.png', 'file4.png', 'file1.py', 'file5.py', 'file8.txt'])

        > (루트경로, 경로에서 존재하는 디렉토리들, 경로에서 존재하는 파일들)
        이 내용을 이용하여 풀이할 수 있음 : "경로에서 존재하는 파일들" 이용
        """
        print(results)


solution3()
