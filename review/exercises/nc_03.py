# data structures

print('---lists---')
# lists
days_of_week = ["월", "화", "수", "목", "금"]

print(days_of_week)
print(days_of_week.count("월"))
# days_of_week.clear()
print(days_of_week.reverse())
print(days_of_week)
print(days_of_week.append("토"))
print(days_of_week.append("일"))
print(days_of_week)

print(days_of_week[3])

lists = [0, "hello", "bye", True, 7]

print('---tuples---')
# tuples → immutable
days = ('월', '화', '수', '목', '금')
print(days.count('월'))
print(days[0])
print(days[-1])
print(days[-2])

print('---dictionary---')
# dictionary
player = {
    'name': 'jjanmo',
    'age': 25,
    'alive': True,
    'fav_food': ['🍕', '🥩']
}
print(player)
print(player['name'])
print(player.get('age'))
print(player.get('fav_food'))

player.pop('age')
print(player)
player['job'] = 'developer'
print(player)
player['fav_food'].append('🍎')
print(player.get('fav_food'))
