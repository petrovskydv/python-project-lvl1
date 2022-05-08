import random


def get_question():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    action = random.choice(('+', '-', '*'))
    return number1, action, number2


def get_question_text(expression):
    return ' '.join(expression)


def get_answer(expression):
    if expression[1] == '+':
        return str(expression[0] + expression[2])
    if expression[1] == '-':
        return str(expression[0] - expression[2])

    return str(expression[0] * expression[2])


def get_game_description():
    return 'What is the result of the expression?'
