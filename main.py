import numpy as np
import string


def get_cell(text):

    test = 'a1'

    column = string.ascii_lowercase.index(text[0])
    row = 8 - int(text[1])

    return [row, column]


arr = np.array([
    ['R', 'C', 'B', 'Q', 'K', 'B', 'C', 'R'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'C', 'B', 'Q', 'K', 'B', 'C', 'R']
])

game_over = False

while not game_over:
    val = input("add your move here (a7 to a6): ")

    if val == 'end':
        game_over = True
    else:
        value_list = val.split()
        old_cell = get_cell(value_list[0])
        new_cell = get_cell(value_list[2])

        figure = arr[old_cell[0]][old_cell[1]]
        arr[old_cell[0]][old_cell[1]] = ' '
        arr[new_cell[0]][new_cell[1]] = figure

        print(arr)
        print()

























