#!/usr/bin/env python
import random

import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        number = random.randint(1, 100)
        print(f'Question: {number}')
        correct_answer = 'yes' if number % 2 == 0 else 'no'
        answer = input('Your answer:')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
            print("Let's try again, {name}!")
            exit()

    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
