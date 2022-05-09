#!/usr/bin/env python
from brain_games.gameplay import play, greet
from brain_games.games.progression import (
    get_game_description,
    get_question,
    get_answer,
    get_question_text,
    get_hidden_index,
)


def main():
    name = greet()
    print(get_game_description())

    question1 = get_question()
    hidden_index1 = get_hidden_index(question1)

    question2 = get_question()
    hidden_index2 = get_hidden_index(question2)

    question3 = get_question()
    hidden_index3 = get_hidden_index(question3)

    questions = (
        get_question_text(question1, hidden_index1),
        get_question_text(question2, hidden_index2),
        get_question_text(question3, hidden_index3),
    )
    answers = (
        get_answer(question1, hidden_index1),
        get_answer(question2, hidden_index2),
        get_answer(question3, hidden_index3),
    )

    if play(questions, answers):
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


if __name__ == '__main__':
    main()
