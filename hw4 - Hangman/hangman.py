# Words were taken from https://github.com/Xethron/Hangman/blob/master/words.txt
import os
import random
from hangman_graphic_print import print_hangman

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
WORDS_PATH = os.path.join(CURRENT_PATH, 'words.txt')
USED_WORDS = ['']
MAX_MOVES_NUM = 11
ALPHABET = list(map(chr, range(97, 123)))


def get_new_word(file_path=WORDS_PATH):
    words = ''
    with open(file_path) as f:
        words = f.read().splitlines()
        word = random.choice(words)
        while word in USED_WORDS and len(USED_WORDS) < len(words):
            word = random.choice(words).lower()
    USED_WORDS.append(word)
    return word


def get_user_input(used_letters):
    user_input = ''
    while user_input not in ALPHABET:
        user_input = input('Please choose a letter: ')
        if user_input in used_letters:
            user_input = ''
    return user_input


def is_game_finished(word, riddle_state, used_letters):
    """
    Returns 1 if game won, -1 if lost, 0 if game is not finished
    """
    wrong_attempts_num = len(used_letters) - len(set(riddle_state)) + 1
    if wrong_attempts_num >= MAX_MOVES_NUM:
        return -1
    elif word == ''.join(riddle_state):
        return 1
    else:
        return 0


def print_field(riddle_state, used_letters):
    # +1 because there is a '_' in riddle_state
    wrong_attempts_num = len(used_letters) - len(set(riddle_state)) + 1
    print()
    print('-' * 20)
    print('Your word looks like: {}'.format(' '.join(riddle_state)))
    print('You\'ve used letters: {}'.format(' '.join(used_letters)))
    print('Attempts left: {}'.format(MAX_MOVES_NUM - wrong_attempts_num))
    print_hangman(wrong_attempts_num)


def print_result(game_finished, word):
    if game_finished == 1:
        print('You won!')
        input('Press Enter key to play another one ')
    if game_finished == -1:
        print('You lost! The word was: {}'.format(word))
        input('Press Enter key to play another one ')


def update_riddle_state(riddle_state, word, letter):
    """
        Checks if letter presents in word. If yes, 
        puts it in positions where it presents in the word
    """
    if letter in word:
        for l in range(len(word)):
            if word[l] == letter:
                riddle_state[l] = letter
    return riddle_state


def main():
    word = get_new_word()
    riddle_state = list('_' * len(word))
    used_letters = []
    game_finished = 0
    while not game_finished:
        print_field(riddle_state, used_letters)
        letter = get_user_input(used_letters)
        used_letters.append(letter)
        riddle_state = update_riddle_state(riddle_state, word, letter)
        game_finished = is_game_finished(
            word, riddle_state, used_letters)
    print_field(riddle_state, used_letters)
    print_result(game_finished, word)


if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nShutting down')
        exit(0)
