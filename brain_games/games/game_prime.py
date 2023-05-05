from random import randint

rules_of_game = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def body_of_games():
    task = randint(1, 100)
    answer_correct = 'yes'
    count = 0

    for i in range(1, task + 1):
        if task % i == 0:
            count += 1

    if count > 2:
        answer_correct = 'no'
    return task, answer_correct
