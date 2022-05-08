import random


def get_question():
    return random.randint(1, 100)


def get_answer(number):
    return 'yes' if number % 2 == 0 else 'no'


def get_game_description():
    return 'Answer "yes" if the number is even, otherwise answer "no".'
