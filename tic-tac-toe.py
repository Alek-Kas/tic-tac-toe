# Крестики-нолики игра для двух игроков
'''
1 приветствие
2 отрисовка поля
3 ход игрока "х" (ввод, проверка на координаты внутри поля, проверка на свободное поле)
4 проверка условий победы или ничьей
5 пункт 2
6 ход игрока "о" (ввод, проверка на координаты внутри поля, проверка на свободное поле)
7 проверка условий победы или ничьей
8 пунк 2
'''

print('Это игра крестики - нолики для двух игроков')
def print_field(args):
    print()
    for i in args:
        for j in i:
            print(j, end = ' ')
        print()
    print()

player = 0
xy = [0, 0]
coord_table = ('a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3')
playing_field = [
    [' ', 'a', 'b', 'c'],
    ['1', '-', '-', '-'],
    ['2', '-', '-', '-'],
    ['3', '-', '-', '-']
]

print_field(playing_field) # вывод поля через фунцию "по слоям"
if player == 0:
    print('Игрок "X" Ваш ход')
else:
    print('Игрок "O" Ваш ход')
coord = None
while coord not in coord_table:
    coord = input('Введите координаты в формате буква столбца и цифра строки, например "b3": ')
    coord = coord.lower()
#    print(type(coord), coord)
for i in coord:
    if i == 'a':
        xy[0] = 1
    elif i == 'b':
        xy[0] = 2
    elif i == 'c':
        xy[0] = 3
    else:
        xy[1] = int(i)
print(xy)