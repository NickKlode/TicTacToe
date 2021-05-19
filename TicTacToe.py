field = [['_' for x in range(3)] for y in range(3)]
vertical_coords = ('0', '1', '2')

selection = input("Выберите 'X' или 'O': ").upper()


def select_sigh(selection):
    while True:
        if selection not in ('X', 'O'):
            print("Неверное значение.")
            selection = input("Выберите 'X' или 'O': ").upper()
            continue
        if selection == 'X' or selection == 'O':
            print(f"Первый игрок выбрал - {selection}")
        break
select_sigh(selection)


def show_field(field):
    print(' ', '0', '1', '2')
    for i, j in enumerate(vertical_coords):
        print(j, ' '.join(field[i]))


def move_coords(field):
    while True:
        coord = input("Введите координаты x - по вертикали и y - по горизонтали: ").split()
        if len(coord) != 2:
            print("Введите два числа через пробел.")
            continue
        elif coord[0].isalpha() or coord[1].isalpha():
            print("Введите цифры.")
            continue
        x, y = int(coord[0]), int(coord[1])
        if not 0 <= x <= 2:
            print(f"Число {x} - вне диапазона.")
            continue
        elif not 0 <= y <= 2:
            print(f"Число {y} - вне диапазона.")
            continue
        if field[x][y] != '_':
            print("Клетка занята.")
            continue
        break
    return x, y


def winner_check(field, player):
    win_list = []
    for w in field:
        win_list += w
    win_pos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    indexes = set([i for i, x in enumerate(win_list) if x == player])
    for p in win_pos:
        if len(indexes.intersection(set(p))) == 3:
            return True
    return False


count = 0
while True:
    if selection == 'X':
        if count % 2 == 0:
            player = 'X'
        else:
            player = 'O'
    else:
        if count % 2 == 0:
            player = 'O'
        else:
            player = 'X'
    show_field(field)
    if count < 9:
        x, y = move_coords(field)
        field[x][y] = player
    if count == 9:
        print("Ничья")
        break
    if winner_check(field, player):
        print(f"Выйграл игрок {player}")
        show_field(field)
        break
    count += 1
