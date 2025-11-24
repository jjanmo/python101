# 43 폴더 하위에서 *.txt, *.png 파일을 분류하기
# Recursive File Extension Checker

import glob


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
