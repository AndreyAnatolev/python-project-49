from random import randint

RULES_OF_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def even_numbered(number):
    if number % 2 == 0:
        return True
    else:
        return False


def body_of_games():
    task = randint(1, 99)
    if even_numbered(task) is True:
        answer_correct = 'yes'
    else:
        answer_correct = 'no'
    return task, answer_correct
