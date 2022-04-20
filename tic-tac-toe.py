# Крестики-нолики игра для двух игроков
'''
План предварительный
1 приветствие
2 отрисовка поля
3 ход игрока "х" (ввод, проверка на координаты внутри поля, проверка на свободное поле)
4 проверка условий победы или ничьей
5 пункт 2
6 ход игрока "о" (ввод, проверка на координаты внутри поля, проверка на свободное поле)
7 проверка условий победы или ничьей
8 пунк 2
'''

print('Это игра крестики - нолики для двух игроков - "X" и "O"')
player = 'X'

def print_field(args):
    print()
    for i in args:
        for j in i:
            print(j, end = ' ')
        print()
    print()

def make_turn(i, j):
    if playing_field[i][j] == '-':
        playing_field[i][j] = player
    else:
        print(f'Сюда ставить "{player}" нельзя, тут уже стоит "{playing_field[i][j]}", повторите ход')
        make_turn(*coord_input())

def coord_input():
    coord = None
    while coord not in coord_table:
        coord = input('Введите координаты в формате буква столбца и цифра строки, например "b3": ')
        coord = coord.lower()
    for i in coord:
        if i == 'a':
            x = 1
        elif i == 'b':
            x = 2
        elif i == 'c':
            x = 3
        else:
            y = int(i)
    return (y, x)

def vic_cond(args):  # условие победы
    p3 = player * 3
    for i in range(1, field_size + 1):
        j_str = ''
        i_str = ''
        x_1 = ''
        x_2 = ''
        for j in range(1, field_size + 1):
            j_str += args[j][i]
            i_str += args[i][j]
            x_1 += args[j][j]
            x_2 += args[j][4 - j]
            if p3 in j_str or p3 in i_str or p3 in x_1 or p3 in x_2:  # как бы это упростить?
                print(f'Конец игры. Победил игрок "{player}"')
                return True

def draw_game_cond(args):  # условие ничьей
    test = True
    for i in args:
        if '-' in i:
            test = False
    if test == True:
        print('Конец игры. Ничья!!!')
    return test

victory = False
draw_game = False
x = 0
y = 0
coord_table = ('a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3')
playing_field = [
    [' ', 'a', 'b', 'c'],
    ['1', '-', '-', '-'],
    ['2', '-', '-', '-'],
    ['3', '-', '-', '-']
]
field_size = len(playing_field) - 1
print_field(playing_field)  # вывод поля через фунцию "по слоям" на первом ходу

while not victory and not draw_game:
    print(f'Игрок "{player}" Ваш ход')
    make_turn(*coord_input())
    print_field(playing_field)
    victory = vic_cond(playing_field)
    if not victory:
        draw_game = draw_game_cond(playing_field)
    if player == 'X':
        player = 'O'
    else:
        player = 'X'