from brain_games.cli import get_name


def play(questions, correct_answers):
    for index in range(3):
        print(f'Question: {questions[index]}')
        answer = input('Your answer:')
        if correct_answers[index] == answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answers[index]}'")
            return False
    return True


def greet():
    print('Welcome to the Brain Games!!!')
    name = get_name()
    print(f'Hello, {name}!')
    return name