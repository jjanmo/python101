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
