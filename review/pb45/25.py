x = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]


# sol1
def split_chunk1(chunk_count, list):
    new_list = []
    chunk = []
    for i, v in enumerate(list):
        if (i + 1) % chunk_count < chunk_count:
            chunk.append(v)
            if len(chunk) == chunk_count:
                new_list.append(chunk)
                chunk = []
        if i == len(list) - 1 and len(chunk) != 0:
            new_list.append(chunk)
    return new_list


# print(split_chunk1(3, x))
# print(split_chunk1(5, x))
# print(split_chunk1(7, x))


# sol2 : range + list slice를 활용 👍🏻
def split_chunk2(chunk_count, list):
    new_list = []
    for i in range(0, len(list), chunk_count):
        new_list.append(list[i : i + chunk_count])
    return new_list


# print(split_chunk2(3, x))
# print(split_chunk2(5, x))
# print(split_chunk2(7, x))


print("######")

# sol3 : List Comprehension 이용 👍🏻
# sol2를 변형!


def split_chunk3(chunk_count, list):
    return [list[i : i + chunk_count] for i in range(0, len(list), chunk_count)]


print(split_chunk3(3, x))
print(split_chunk3(5, x))
print(split_chunk3(7, x))
