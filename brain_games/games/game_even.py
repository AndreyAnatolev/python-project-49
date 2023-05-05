from random import randint

rules_of_game = 'Answer "yes" if the number is even, otherwise answer "no".'


def body_of_games():
    task = randint(1, 99)
    if task % 2 == 0:
        answer_correct = 'yes'
    else:
        answer_correct = 'no'
    return task, answer_correct
