import random


def get_question():
    return random.randint(1, 100)


def get_question_text(number):
    return str(number)


def get_answer(number):
    return 'yes' if is_prime(number) else 'no'


def is_prime(number):
    divider = 2
    while number % divider != 0:
        divider += 1
    return divider == number


def get_game_description():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'
