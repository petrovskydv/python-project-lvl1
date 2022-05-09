import random


def get_question():
    count = 9
    step = random.randint(1, 5)
    start = random.randint(1, 20)

    sequence = [start]
    for _ in range(count):
        start += step
        sequence.append(start)

    return sequence


def get_question_text(numbers, hidden_index):
    # text = ''
    # for index in range(len(numbers)):  # noqa: WPS518
    #     if index == hidden_index:
    #         text = ' '.join([text, '..'])
    #     else:
    #         text = ' '.join([text, str(numbers[index])])

    text = ' '.join(
        '..' if number == numbers[hidden_index] else str(number) for number in numbers
    )
    return text


def get_answer(numbers, hidden_index):
    return str(numbers[hidden_index])


def get_hidden_index(numbers):
    return random.randint(3, len(numbers) - 2)


def get_game_description():
    return 'Find the greatest common divisor of given numbers.'
