import random


def get_question():
    return random.randint(1, 100)


def get_answer(number):
    return 'yes' if is_prime(number) else 'no'


def is_prime(number):
    if number < 2:
        return False

    divider = 2

    while divider <= number / 2:
        if number % divider == 0:
            return False
        divider += 1

    return True


def get_game_description():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'
