# Не могу утверждать, что это моя самостоятельная работа.
# Ибо не способен пока с легкостью оперировать полученными знаниями и очень ограничен во времени для закрепления их.
# За основу взят код из вебинара. Не знаю как Вы это оцените.
# С уважением, Ваш студент!

def welcome():
    print('=======================')
    print('|   Приветсвуем Вас   |')
    print('|        в игре       |')
    print('|  "Крестики-Нолики"  |')
    print('=======================')
    print('|  Формат ввода: x y  |')
    print('|  x - номер строки   |')
    print('|  y - номер столбца  |')
    print('=======================')


def playing_field():
    print()
    print("    || 0 | 1 | 2 || ")
    print("  ================= ")
    for i, row in enumerate(field):
        row_str = f"  {i} || {' | '.join(row)} || "
        print(row_str)
        print("  _________________  ")
    print()


def ask():
    while True:
        coordinate = input("  Ваши координаты: ").split()

        if len(coordinate) != 2:
            print(' Введите координаты "x" и "y" через пробел: ')
            continue

        x, y = coordinate

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Не верные координаты! ")
            continue

        if field[x][y] != " ":
            print(" Координата занята! ")
            continue

        return x, y


def check_win():
    win_coordinate = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for coordinate in win_coordinate:
        symbols = []
        for c in coordinate:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False


welcome()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    playing_field()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print(" Ничья!")
        break