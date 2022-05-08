import random


def get_question():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    return number1, number2


def get_question_text(expression):
    return f'{expression[0]} {expression[1]}'  # noqa: WPS221


def get_answer(numbers):
    number1, number2 = numbers
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 %= number2
        else:
            number2 %= number1

    return str(number1 + number2)


def get_game_description():
    return 'Find the greatest common divisor of given numbers.'
