# -*- coding: utf-8 -*-

# `random` module is used to shuffle field, see§:
# https://docs.python.org/3/library/random.html#random.shuffle
import random
from sys import exit

# Empty tile, there's only one empty cell on a field:
EMPTY_MARK = 'x'

# Dictionary of possible moves if a form of:
# key -> delta to move the empty tile on a field.
MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}

# Dictionary of possible wrong moves indexes:
# key -> index from which you cannot make a corresponding move
WRONG_MOVE_INDEXES = {
    'w': (0, 1, 2, 3),
    's': (12, 13, 14, 15),
    'a': (0, 4, 8, 12),
    'd': (3, 7, 11, 15)
}


def shuffle_field():
    """
    This method is used to create a field at the very start of the game.
    :return: list with 16 randomly shuffled tiles,
    one of which is a empty space.
    """
    field = list(range(1, 16))
    field.append(EMPTY_MARK)
    moves = list(MOVES)
    for i in range(1000):
        while True:
            try:
                field = perform_move(field, random.choice(moves))
                break
            except IndexError:
                continue
    return field


def print_field(field):
    """
    This method prints field to user.
    :param field: current field state to be printed.
    :return: None
    """
    print('-' * 19)
    for i in range(len(field)):
        print('{0:^3}|'.format(field[i]), end=' ',)
        if (i + 1) % 4 == 0:
            print('\n' + '-' * 19)


def is_game_finished(field):
    """
    This method checks if the game is finished.
    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    finished_field = list(range(1, 16))
    finished_field.append(EMPTY_MARK)
    return field == finished_field


def perform_move(field, key):
    """
    Moves empty-tile inside the field.
    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move).
    :raises: IndexError if the move can't me done.
    """
    mark_index = field.index(EMPTY_MARK)
    new_index = mark_index + MOVES[key]
    if mark_index in WRONG_MOVE_INDEXES[key]:
        raise IndexError
    # Fine, move it
    field[mark_index], field[new_index] = field[new_index], field[mark_index]
    return field


def handle_user_input():
    """
    Handles user input. List of accepted moves:
        'w' - up, 
        's' - down,
        'a' - left, 
        'd' - right
    :return: <str> current move.
    """
    while True:
        move = input('Your move (wasd): ')
        if len(move) == 1 and move in MOVES:
            return move
        else:
            continue


def main():
    """
    The main method. It stars when the program is called.
    It also calls other methods.
    :return: None
    """
    field = shuffle_field()
    move_count = 0
    print_field(field)
    while not is_game_finished(field):
        try:
            move = handle_user_input()
            field = perform_move(field, move)
        except IndexError:
            print('Move cannot be performed, please enter correct move.')
            continue
        move_count += 1
        print('\n')
        print_field(field)

    print('Victory! You\'v made {} moves.'.format(move_count))


if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do
    try:
        main()
    except KeyboardInterrupt:
        print('\nshutting down')
        exit(0)
