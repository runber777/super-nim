import random

alphabet = 'abcdefgh'
array = [
    [
        "○" for _ in range(8)
    ] for _ in range(1, 8 + 1)
]


def random_num():  # Генерирует случайные числа
    random_number = random.randint(1, 64)
    return random_number


def place_random_buttons():  # Расстановка пуговиц по полю
    random_number = random_num()
    for i in range(random_number):
        random_row = random.randint(0, 7)
        random_col = random.randint(0, 7)
        array[random_row][random_col] = '●'


def remove_row(selected_row):  # Удаление пуговиц со строки
    row_index = alphabet.find(selected_row)
    for element_index in range(0, len(array[row_index])):
        array[row_index][element_index] = "○"


def remove_column(selected_column):  # Удаление пуговиц со столбца
    column_index = selected_column - 1
    for row_index in range(8):
        array[row_index][column_index] = "○"


def select_move(): # Выбор хода
    move = input('Выберите a-h (столбец)/1-8 (ряд): ')
    make_move(move)


def check_row(selected_row): # Проверка строки
    row_index = alphabet.find(selected_row)
    if "●" in array[row_index]:
        return True
    return False


def check_column(selected_column): # Проверка столбца
    column_index = selected_column - 1
    for row_index in range(8):
        if array[row_index][column_index] == "●":
            return True
    return False


def make_move(move): # Механика хода
    if move == "":
        select_move()
    try:
        move = int(move)
        if (1 <= move <= 8) and check_column(move):
            remove_column(move)
        else:
            select_move()
    except ValueError:
        if (move in alphabet) and (check_row(move)):
            remove_row(move)
        else:
            select_move()


def check_array(): # Проверка поля
    for row in array:
        for element in row:
            if element == "○":
                continue
            else:
                return True
    return False


def moves_check(current_move): # Проверка ходов
    if current_move == 0:
        current_move = 2
    fisrt_player_move = input(f"Ход {current_move} игрока. Выберите столбец/ряд: ")
    make_move(fisrt_player_move)
    field()
    result = current_move
    if check_array():
        current_move = (current_move + 1) % 2
        result = moves_check(current_move)
    return result


def field(): # Генерация поля
    print('––––––––––––––––––– |')
    index = 0
    for row in array:
        print(alphabet[index], "|", *row, "|")
        index += 1
    print("––––––––––––––––––– |")
    print("  |", *[str(i) for i in range(1, 8 + 1)], "|")


def game():
    place_random_buttons()
    field()
    current_move = 1
    winner = moves_check(current_move)
    print(f'Победитель: {winner} игрок!')


game()
