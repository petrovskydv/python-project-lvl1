from brain_games.gameplay import play, greet
from brain_games.games.calc import get_game_description, get_question, get_answer


def main():
    name = greet()
    print(get_game_description())

    question1 = get_question()
    answer1 = get_answer(question1)
    question2 = get_question()
    answer2 = get_answer(question2)
    question3 = get_question()
    answer3 = get_answer(question3)

    questions = (question1, question2, question3)
    answers = (answer1, answer2, answer3)

    if play(questions, answers):
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


if __name__ == '__main__':
    main()
