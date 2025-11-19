# 42 폴더에 있는 파일 중에 확장자가 *.py, *.png 인 것을 분류하세요

"""
출력결과
PNG 파일 정보 : ['file10.png', 'file11.png', 'file19.png', 'file6.png'] 총 4개
PY 파일 정보 : ['file12.py', 'file13.py', 'file17.py', 'file3.py', 'file4.py', 'file8.py' ] 총 6개
"""

from pathlib import Path


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
