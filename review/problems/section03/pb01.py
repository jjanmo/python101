def solution(n, array):
    for i in range(n):
        word = array[i].lower()
        for k in range(len(word) // 2):
            if word[k] != word[-(k + 1)]:
                print(f'#{i + 1} NO')
                break
        else:
            print(f'#{i + 1} YES')


solution(5, ['level', 'moon', 'abcba', 'soon', 'gooG'])
print('---------')
solution(7, ['stts', 'moon', 'abcba', 'yes', 'goodboy', 'stttttts', 'tttttttttttttt'])
print('---------')
solution(20, [
    'skgjkjdkjgkksjgk',
    'sssssssssssssssksssssssssssssss',
    'jtbccbtj',
    'kakakakakakakakaakakakakakakak',
    'bigtodtheb',
    'itistimetosutudyydutusotemitsiti',
    'kdjglks',
    'osdddddddddddddddddddddddso',
    'sksdddddddddddddddddddddddddddddddddddddddkss',
    'skskskuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuksksks',
    'stts',
    'moon',
    'kskgjkljdlkjlkjkdjglksjlkdjglkdjd',
    'studenttneduts',
    'kstudkgksjlkgjlksjdggkkllllllllllllllllllllllsjgksjldgjlllllllllllllllgjks',
    'abcba',
    'djfkljlkgjklsjklglksjdlg',
    'dkjglskjdkjgls',
    'yes',
    'goodboy',
])


# 단순 문자열 한개가 들어왔다고 가정
def solution2(string):
    new_str = string.lower()
    if new_str == new_str[::-1]:  # [::-1] 거꾸로 슬라이싱
        print('회문이다')
    else:
        print('회문 아니다')
