# 42 폴더에 있는 파일 중에 확장자가 *.py, *.png 인 것을 분류하세요

"""
출력결과
PNG 파일 정보 : ['file10.png', 'file11.png', 'file19.png', 'file6.png'] 총 4개
PY 파일 정보 : ['file12.py', 'file13.py', 'file17.py', 'file3.py', 'file4.py', 'file8.py' ] 총 6개
"""

from pathlib import Path
import os
import glob


def solution(folder_path):
    path = Path(folder_path)

    images = []
    pys = []
    for p in path.iterdir():
        if p.is_file() and p.suffix == ".png":
            images.append(p.name)
        if p.is_file() and p.suffix == ".py":
            pys.append(p.name)

    return sorted(images), sorted(pys)


def format(image_list, py_list):
    print(f"PNG 파일 정보 : [ {', '.join(image_list)} ] 총 {len(image_list)}개")
    print(f"PY 파일 정보 : [ {', '.join(py_list)} ] 총 {len(py_list)}개")


image_list, py_list = solution("./42")
format(image_list, py_list)


def solution2(path):
    files = os.listdir(
        path
    )  # 파일인지 폴더인지 구분이 안됨 > 여기서는 파일이라고 가정하고 품
    png_files = sorted(list(filter(lambda f: f.endswith("png"), files)))
    python_files = sorted(list(filter(lambda f: f.endswith("py"), files)))
    format(png_files, python_files)


solution2("./42")


def solution3():
    # glob.glob(파일경로(+패턴), recursive여부=False) > 리턴값 매칭되는 파일, 디렉토리 경로들의 리스트 반환
    # ex. ['./42/file19.png', './42/file6.png', './42/file10.png', './42/file11.png']

    png_files = sorted(list(map(lambda s: s.split("/")[-1], glob.glob("./42/*.png"))))
    python_files = sorted(list(map(lambda s: s.split("/")[-1], glob.glob("./42/*.py"))))
    format(png_files, python_files)


solution3()
